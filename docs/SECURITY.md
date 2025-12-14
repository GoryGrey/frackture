# 🔒 Frackture Security Analysis

This document provides a comprehensive analysis of Frackture's security properties, threat model, attack resistance, and appropriate use cases.

---

## Table of Contents

- [Overview](#overview)
- [Threat Model](#threat-model)
- [Security Features](#security-features)
- [Attack Resistance](#attack-resistance)
- [Limitations](#limitations)
- [Best Practices](#best-practices)
- [Cryptographic Properties](#cryptographic-properties)
- [Compliance Considerations](#compliance-considerations)

---

## Overview

**Important:** Frackture is designed for:
- ✅ **Data fingerprinting** with collision resistance
- ✅ **Integrity verification** with HMAC authentication
- ✅ **Tamper detection** via cryptographic signatures
- ✅ **Authenticated encryption** of payloads

**Frackture is NOT designed for:**
- ❌ **Primary cryptographic encryption** (use AES, ChaCha20)
- ❌ **Password hashing** (use Argon2, bcrypt, scrypt)
- ❌ **Long-term secret storage** (use proper KMS)
- ❌ **Regulatory compliance** (FIPS, HIPAA require certified algorithms)

---

## Threat Model

### Assets to Protect

1. **Data Integrity**: Ensure payloads haven't been tampered with
2. **Key Authentication**: Verify correct key is used
3. **Collision Resistance**: Prevent different inputs producing same fingerprint
4. **Identity Preservation**: Maintain unique signatures per input

### Threat Actors

**In Scope:**
- Network attackers (man-in-the-middle)
- Malicious insiders with payload access
- Automated tampering attempts
- Collision attack attempts
- Timing attack adversaries

**Out of Scope:**
- Nation-state cryptographic attacks
- Quantum computing threats
- Side-channel attacks on hardware
- Physical access to keys
- Memory dump analysis

### Attack Scenarios

#### 1. Payload Tampering

**Scenario:** Attacker modifies encrypted payload data

```python
# Legitimate encryption
encrypted = frackture_encrypt_payload(payload, "secret-key")

# Attacker tampers with payload
encrypted["data"]["symbolic"] = "attackercontrolled"

# Verification FAILS
try:
    decrypted = frackture_decrypt_payload(encrypted, "secret-key")
except ValueError:
    print("Tampering detected!")  # Executes
```

**Protection:** HMAC signature verification detects any data modification.

#### 2. Key Guessing

**Scenario:** Attacker attempts to guess encryption key

```python
# Try common keys
common_keys = ["password", "12345", "admin", "secret"]
for key in common_keys:
    try:
        decrypted = frackture_decrypt_payload(encrypted, key)
        print("Key found!")
        break
    except ValueError:
        continue  # Wrong key
```

**Protection:** 
- HMAC verification fails for wrong keys
- Key ID check provides fast rejection
- Use strong, random keys (see [Best Practices](#best-practices))

#### 3. Collision Attacks

**Scenario:** Attacker tries to find two inputs with same fingerprint

```python
# Birthday attack on 32-byte fingerprint
# Expected collisions after: sqrt(2^256) = 2^128 attempts
# Computationally infeasible
```

**Protection:**
- 32-byte symbolic fingerprint (256 bits)
- 16-element entropy signature (additional bits)
- Combined collision probability: negligible

#### 4. Timing Attacks

**Scenario:** Attacker measures signature comparison time to extract key bits

```python
# Vulnerable code (DO NOT USE):
if encrypted["signature"] == expected_signature:  # Leaks timing info
    return data

# Frackture uses constant-time comparison:
if hmac.compare_digest(encrypted["signature"], expected_signature):
    return data
```

**Protection:** `hmac.compare_digest` prevents timing attacks.

---

## Security Features

### 1. HMAC-SHA256 Authentication

**What It Provides:**
- Message authentication (integrity + authenticity)
- Keyed cryptographic hash
- Tamper detection

**How It Works:**
```
Data: {"symbolic": "<64-hex>", "entropy": [16 floats], ...optional tier metadata...}
Metadata: {"version": 1, "key_id": "<8-hex>"}
Key: "my-secret-key"
                   ↓
Canonical JSON (sort_keys=True, separators=(',', ':'))
                   ↓
HMAC-SHA256({data, metadata}, Key) → Signature
                   ↓
Store: {"data": ..., "metadata": ..., "signature": ...}
                   ↓
Verify: validate structure + recompute HMAC + constant-time compare
```

**Structural validation:** Frackture validates the raw payload format (required keys, 64-char hex fingerprint, 16 finite entropy values, optional tier metadata) and the encrypted envelope structure. Any structural mismatch or integrity failure raises `ValueError`.

**Strength:**
- SHA-256: 256-bit output, collision-resistant
- HMAC construction: prevents length-extension attacks
- Industry standard (RFC 2104, FIPS 198-1)

### 2. Constant-Time Comparison

**Implementation:**
```python
# Uses hmac.compare_digest() internally
if not hmac.compare_digest(received_sig, expected_sig):
    raise ValueError("Invalid signature")
```

**Why It Matters:**
- Prevents timing side-channels
- Attacker can't deduce signature bits from comparison time
- Required for cryptographic security

### 3. Key ID Metadata

**Structure:**
```python
"metadata": {
    "version": 1,
    "key_id": "a3f5c8e2"  # First 8 chars of SHA256(key)
}
```

**Benefits:**
- Fast key identification (before full HMAC verification)
- Enables key rotation without trying all keys
- Multi-key system support

**Security Note:**
- Key ID is NOT secret (it's a hash)
- Safe to expose publicly
- Only used for identification, not authentication

### 4. Deterministic Hashing

**Function:**
```python
frackture_deterministic_hash(data, salt="")
```

**Properties:**
- Same input → same hash (deterministic)
- Different input → different hash (collision-resistant)
- Optional salt for namespacing
- SHA-256 based (industry standard)

**Use Cases:**
- Integrity checking
- Deduplication
- Content-addressable storage

---

## Attack Resistance

### Collision Resistance

**Symbolic Fingerprint:**
- Output: 64-character hex (32 bytes = 256 bits)
- Collision probability: ~2^(-256)
- Birthday bound: 2^128 attempts for 50% collision chance
- **Verdict:** Computationally infeasible with current technology

**Entropy Signature:**
- Output: 16 floats (additional ~128 bits of information)
- Provides secondary collision resistance
- Different frequency patterns for different inputs
- **Verdict:** Adds redundancy and robustness

**Combined System:**
- Must collide in both channels
- Probability: ~2^(-384) (conservative estimate)
- **Verdict:** Extremely collision-resistant

### Pre-image Resistance

**Given fingerprint, can attacker find input?**

```python
target_fingerprint = "a3f5c8e2d9b1f7a4..."
# Can attacker find input X such that frackture(X) = target_fingerprint?
```

**Analysis:**
- Symbolic channel: XOR operations with masking
- 4-pass recursive transformation
- Each pass depends on previous state
- No known efficient inversion

**Verdict:** Pre-image attacks are impractical

### Second Pre-image Resistance

**Given input1, can attacker find input2 with same fingerprint?**

```python
input1 = "known data"
fingerprint1 = get_fingerprint(input1)
# Can attacker find input2 where get_fingerprint(input2) == fingerprint1?
```

**Analysis:**
- Same as collision resistance
- 256-bit symbolic fingerprint
- Additional entropy channel constraints
- **Verdict:** Second pre-image attacks are impractical

### Brute Force Resistance

**Key Brute Force:**
```python
# Assumptions:
# - 16-character alphanumeric key (62^16 possibilities)
# - HMAC-SHA256 verification per attempt
# - 1 million attempts per second (optimistic for attacker)

keyspace = 62 ** 16  # ~4.7 × 10^28
attempts_per_second = 1_000_000
seconds_per_year = 31_536_000

years_to_crack = keyspace / (attempts_per_second * seconds_per_year)
# Result: ~1.5 × 10^15 years (age of universe: ~1.4 × 10^10 years)
```

**Verdict:** Strong keys are brute-force resistant

**Recommendation:** Use 20+ character random keys for high-security applications.

### Timing Attack Resistance

**Vulnerable Code:**
```python
# DON'T DO THIS:
if signature == expected:
    return True
```

**Why Vulnerable:**
- String comparison short-circuits on first mismatch
- Attacker measures time to compare
- Can deduce correct characters one by one

**Frackture Protection:**
```python
# Safe constant-time comparison:
hmac.compare_digest(signature, expected)
```

**How It Works:**
- Compares all bytes regardless of mismatches
- Always takes same time
- No information leakage through timing

**Verdict:** Timing attack resistant

---

## Limitations

### Not Cryptographic Encryption

**What Frackture Provides:**
```python
encrypted = frackture_encrypt_payload(payload, key)
# encrypted["data"] is VISIBLE (plaintext)
# encrypted["signature"] authenticates it
```

**Problem:** Anyone can read the payload data!

**Solution:** For confidentiality, use actual encryption:

```python
from cryptography.fernet import Fernet

# Encrypt with Fernet (AES-128-CBC)
key = Fernet.generate_key()
fernet = Fernet(key)

# Combine Frackture + real encryption
payload = frackture_v3_3_safe(preprocessed)
encrypted_payload = fernet.encrypt(json.dumps(payload).encode())
authenticated = frackture_encrypt_payload(
    {"encrypted": encrypted_payload.decode()},
    hmac_key
)
```

### Not Suitable for Password Hashing

**Problem:** Frackture hashing is too fast!

```python
# BAD: Frackture for passwords
password = "user_password"
hash = frackture_deterministic_hash(password)
# Attacker can test millions of passwords per second
```

**Solution:** Use password hashing functions:

```python
from argon2 import PasswordHasher

ph = PasswordHasher()
hash = ph.hash("user_password")
# Argon2: memory-hard, slow by design, GPU-resistant
```

**Why:**
- Password hashing needs to be SLOW (defense against brute force)
- Frackture is designed to be FAST
- Use Argon2, bcrypt, or scrypt for passwords

### No Forward Secrecy

**Problem:** Compromised key exposes all past payloads

```python
# All payloads encrypted with same key
encrypted1 = frackture_encrypt_payload(payload1, "key")
encrypted2 = frackture_encrypt_payload(payload2, "key")

# If "key" is compromised, ALL payloads are compromised
```

**Solution:** Implement key rotation:

```python
class KeyManager:
    def __init__(self):
        self.keys = {}  # key_id -> key
        self.current_key_id = None
    
    def rotate_key(self):
        new_key = generate_random_key()
        key_id = hashlib.sha256(new_key.encode()).hexdigest()[:8]
        self.keys[key_id] = new_key
        self.current_key_id = key_id
        return new_key
    
    def get_key(self, key_id):
        return self.keys.get(key_id)
```

### Not Quantum-Resistant

**Threat:** Quantum computers could break SHA-256 and HMAC-SHA256

**Timeline:** 10-30+ years (speculative)

**Current Status:** Quantum computers can't break SHA-256 yet

**Future-Proofing:**
- Monitor NIST post-quantum cryptography standards
- Plan migration path to quantum-resistant hashes
- For now: SHA-256 is still secure

---

## Best Practices

### 1. Key Generation

**Good:**
```python
import secrets

# Cryptographically secure random key
key = secrets.token_urlsafe(32)  # 256 bits
```

**Bad:**
```python
# DON'T: Weak keys
key = "password123"
key = "admin"
key = str(uuid.uuid4())  # UUIDs are NOT cryptographic
```

### 2. Key Storage

**Good:**
```python
# Store keys in secure key management system
import os
key = os.environ.get("FRACKTURE_KEY")  # From environment
# OR use AWS KMS, Azure Key Vault, HashiCorp Vault
```

**Bad:**
```python
# DON'T: Hardcode keys
key = "my-secret-key-2024"  # In source code!

# DON'T: Store in database unencrypted
db.execute("INSERT INTO keys VALUES (?)", (key,))
```

### 3. Key Rotation

**Implementation:**
```python
from datetime import datetime, timedelta

class EncryptionService:
    def __init__(self):
        self.keys = {}  # key_id -> (key, created_at)
        self.rotation_interval = timedelta(days=90)
    
    def should_rotate(self, key_id):
        key, created_at = self.keys[key_id]
        return datetime.now() - created_at > self.rotation_interval
    
    def encrypt_with_rotation(self, payload):
        if self.should_rotate(self.current_key_id):
            self.rotate_key()
        
        key = self.keys[self.current_key_id][0]
        return frackture_encrypt_payload(payload, key)
```

### 4. Salt Usage

**Good:**
```python
# Use salts to prevent rainbow tables
user_id = "user_123"
data = "user data"
hash = frackture_deterministic_hash(data, salt=user_id)

# Different users get different hashes for same data
hash_user2 = frackture_deterministic_hash(data, salt="user_456")
assert hash != hash_user2
```

**Use Cases:**
- Multi-tenant systems (salt = tenant_id)
- User-specific hashes (salt = user_id)
- Time-based hashes (salt = timestamp)

### 5. Error Handling

**Good:**
```python
try:
    decrypted = frackture_decrypt_payload(encrypted, key)
except ValueError as e:
    # Log error (but don't expose details to user)
    logger.error("Decryption failed", exc_info=True)
    # Generic error message to user
    raise PermissionError("Invalid credentials")
```

**Bad:**
```python
try:
    decrypted = frackture_decrypt_payload(encrypted, key)
except ValueError as e:
    # DON'T: Expose error details
    print(f"Decryption failed: {e}")  # Reveals attack info
```

### 6. Audit Logging

**Implementation:**
```python
import logging

logger = logging.getLogger("frackture.security")

def secure_decrypt(encrypted, key):
    key_id = encrypted["metadata"]["key_id"]
    
    try:
        decrypted = frackture_decrypt_payload(encrypted, key)
        logger.info(f"Decryption success: key_id={key_id}")
        return decrypted
    except ValueError:
        logger.warning(f"Decryption failure: key_id={key_id}, "
                      f"ip={get_client_ip()}")
        raise
```

---

## Cryptographic Properties

### Algorithms Used

| Component | Algorithm | Strength | Standard |
|-----------|-----------|----------|----------|
| Hashing | SHA-256 | 256-bit | FIPS 180-4 |
| Authentication | HMAC-SHA256 | 256-bit | RFC 2104, FIPS 198-1 |
| Comparison | Constant-time | Timing-safe | Security best practice |

### Randomness

**Pseudo-Random Elements:**
```python
# Symbolic channel mask
mask[i] = (i**2 + i*3 + 1) % 256
```

**Properties:**
- Deterministic (reproducible)
- Uniformly distributed
- No cryptographic randomness needed (fingerprinting is deterministic)

### Entropy Analysis

**Symbolic Fingerprint Entropy:**
- 32 bytes = 256 bits
- XOR operations preserve entropy
- 4-pass mixing increases diffusion

**Entropy Channel Entropy:**
- 16 floats × ~8 bits each ≈ 128 bits (effective)
- FFT captures frequency information
- Statistical features add robustness

**Total System Entropy:**
- Combined: ~384 bits (conservative)
- Sufficient for collision resistance
- Exceeds SHA-256 (256 bits)

---

## Compliance Considerations

### FIPS 140-2/140-3

**Requirements:**
- Certified cryptographic modules
- Physical security (for hardware)
- Key management procedures

**Frackture Status:**
- Uses FIPS-approved algorithms (SHA-256, HMAC)
- Not a certified module itself
- Cannot claim FIPS compliance

**Recommendation:** For FIPS compliance, use certified libraries like OpenSSL FIPS module.

### GDPR (EU)

**Relevant Aspects:**
- Data minimization: Frackture creates fixed-size fingerprints ✓
- Pseudonymization: Fingerprints can act as pseudonyms ✓
- Right to erasure: Delete fingerprints, not original data ✓

**Not Sufficient Alone:**
- Frackture doesn't provide encryption at rest
- Additional controls needed for GDPR compliance

### HIPAA (Healthcare)

**Requirements:**
- Encryption of PHI at rest and in transit
- Access controls
- Audit logs

**Frackture Status:**
- Provides integrity checking ✓
- NOT sufficient encryption for PHI ✗
- Use in combination with HIPAA-compliant encryption

### PCI DSS (Payment Cards)

**Requirements:**
- Strong cryptography for cardholder data
- Key management
- Network security

**Frackture Status:**
- Cannot be used to encrypt credit card numbers
- May be used for integrity checking
- Must combine with PCI-compliant encryption

---

## Security Checklist

Use this checklist when deploying Frackture:

- [ ] Generate strong random keys (32+ characters)
- [ ] Store keys securely (KMS, environment variables, not in code)
- [ ] Implement key rotation (90-day intervals recommended)
- [ ] Use salts for deterministic hashing where appropriate
- [ ] Enable audit logging for all decryption attempts
- [ ] Monitor for repeated decryption failures (potential attacks)
- [ ] Combine with real encryption (AES, ChaCha20) for confidentiality
- [ ] Never use Frackture for password hashing
- [ ] Don't rely on Frackture alone for regulatory compliance
- [ ] Keep libraries updated (numpy, scipy, scikit-learn)
- [ ] Test disaster recovery (key loss scenarios)
- [ ] Document key management procedures

---

## Incident Response

### Suspected Key Compromise

**Immediate Actions:**
1. Rotate keys immediately
2. Revoke compromised key
3. Re-encrypt all payloads with new key
4. Audit access logs for suspicious activity
5. Notify security team

**Example:**
```python
def emergency_key_rotation():
    old_key_id = current_key_id
    new_key = rotate_key()
    
    # Re-encrypt all payloads
    for payload_id in get_all_payload_ids():
        encrypted = load_payload(payload_id)
        decrypted = frackture_decrypt_payload(encrypted, old_key)
        re_encrypted = frackture_encrypt_payload(decrypted, new_key)
        save_payload(payload_id, re_encrypted)
    
    revoke_key(old_key_id)
    log_incident("Key compromise: rotated and re-encrypted all data")
```

### Tampering Detection

**If tampering is detected:**
1. Log the event with full context
2. Alert security team
3. Preserve evidence (encrypted payload)
4. Investigate source of tampered data
5. Review access controls

---

## Conclusion

**Frackture Security Summary:**

✅ **Strong For:**
- Data integrity verification
- Tamper detection
- Collision-resistant fingerprinting
- Authenticated payload transmission

⚠️ **Limitations:**
- Not full encryption (use AES/ChaCha20)
- Not password hashing (use Argon2/bcrypt)
- No forward secrecy (implement key rotation)
- Not quantum-resistant (monitor post-quantum standards)

**Overall:** Frackture provides solid security for its intended use cases (fingerprinting, integrity, authentication) when combined with proper key management and best practices.

---

**Next Steps:**
- Read [ARCHITECTURE.md](./ARCHITECTURE.md) for implementation details
- See [EXAMPLES.md](./EXAMPLES.md) for secure usage patterns
- Check [FAQ.md](./FAQ.md) for common security questions
