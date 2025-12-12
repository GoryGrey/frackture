# 📚 Frackture Examples

This document provides copy-pastable examples for all Frackture workflows, from basic usage to advanced patterns.

---

## Table of Contents

- [Basic Usage](#basic-usage)
- [Compression & Fingerprinting](#compression--fingerprinting)
- [Encryption & Decryption](#encryption--decryption)
- [Hashing & Integrity](#hashing--integrity)
- [Self-Optimization](#self-optimization)
- [Advanced Patterns](#advanced-patterns)
- [Integration Examples](#integration-examples)
- [Error Handling](#error-handling)

---

## Basic Usage

### Minimal Example

```python
# Import from the module
import sys
import importlib.util

# Load frackture module
spec = importlib.util.spec_from_file_location("frackture", "frackture (2).py")
frackture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frackture)

# Use the functions
from frackture import (
    frackture_preprocess_universal_v2_6 as preprocess,
    frackture_v3_3_safe as compress,
    frackture_v3_3_reconstruct as decompress
)

# Process data
data = "Hello, Frackture!"
preprocessed = preprocess(data)
payload = compress(preprocessed)
reconstructed = decompress(payload)

print(f"Original: {data}")
print(f"Payload size: ~{len(payload['symbolic']) + len(payload['entropy']) * 8} bytes")
print(f"Reconstructed shape: {reconstructed.shape}")
```

### Quick Import Helper

Create an import helper for easier usage:

```python
# frackture_helper.py
import sys
import importlib.util
import os

def load_frackture():
    """Load frackture module regardless of filename"""
    module_path = os.path.join(os.path.dirname(__file__), 'frackture (2).py')
    spec = importlib.util.spec_from_file_location("frackture", module_path)
    frackture = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(frackture)
    return frackture

# Usage:
frackture = load_frackture()
preprocessed = frackture.frackture_preprocess_universal_v2_6("data")
```

---

## Compression & Fingerprinting

### Basic Fingerprinting

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe
)

def create_fingerprint(data):
    """Create a fixed-size fingerprint for any data"""
    preprocessed = frackture_preprocess_universal_v2_6(data)
    payload = frackture_v3_3_safe(preprocessed)
    return payload

# Example usage
documents = [
    "The quick brown fox jumps over the lazy dog",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    "Hello, World! This is a test document."
]

fingerprints = {}
for i, doc in enumerate(documents):
    fingerprint = create_fingerprint(doc)
    fingerprints[f"doc_{i}"] = fingerprint
    print(f"Document {i} fingerprint (symbolic): {fingerprint['symbolic'][:32]}...")
```

### File Fingerprinting

```python
import os
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe
)

def fingerprint_file(filepath):
    """Create fingerprint for a file"""
    with open(filepath, 'rb') as f:
        data = f.read()
    
    preprocessed = frackture_preprocess_universal_v2_6(data)
    payload = frackture_v3_3_safe(preprocessed)
    
    return {
        'filename': os.path.basename(filepath),
        'size': len(data),
        'fingerprint': payload['symbolic'],
        'entropy': payload['entropy']
    }

# Example
file_info = fingerprint_file("document.pdf")
print(f"File: {file_info['filename']}")
print(f"Size: {file_info['size']} bytes")
print(f"Fingerprint: {file_info['fingerprint'][:32]}...")
```

### Deduplication System

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe
)
import json

class DeduplicationStore:
    def __init__(self):
        self.fingerprints = {}  # fingerprint -> data_id
        self.data = {}  # data_id -> actual data
    
    def add_data(self, data_id, data):
        """Add data, store only if unique"""
        preprocessed = frackture_preprocess_universal_v2_6(data)
        payload = frackture_v3_3_safe(preprocessed)
        fingerprint = payload['symbolic']
        
        if fingerprint in self.fingerprints:
            print(f"Duplicate detected! {data_id} matches {self.fingerprints[fingerprint]}")
            return False
        else:
            self.fingerprints[fingerprint] = data_id
            self.data[data_id] = data
            print(f"Stored new data: {data_id}")
            return True
    
    def find_duplicates(self):
        """Find any duplicate fingerprints"""
        reverse_map = {}
        for fp, data_id in self.fingerprints.items():
            if fp not in reverse_map:
                reverse_map[fp] = []
            reverse_map[fp].append(data_id)
        
        duplicates = {fp: ids for fp, ids in reverse_map.items() if len(ids) > 1}
        return duplicates

# Example usage
store = DeduplicationStore()
store.add_data("doc1", "Hello World")
store.add_data("doc2", "Hello World")  # Duplicate
store.add_data("doc3", "Different data")
```

### Similarity Detection

```python
import numpy as np
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe
)

def calculate_similarity(data1, data2):
    """Calculate similarity between two inputs using entropy channels"""
    prep1 = frackture_preprocess_universal_v2_6(data1)
    prep2 = frackture_preprocess_universal_v2_6(data2)
    
    payload1 = frackture_v3_3_safe(prep1)
    payload2 = frackture_v3_3_safe(prep2)
    
    # Use entropy channels for similarity
    entropy1 = np.array(payload1['entropy'])
    entropy2 = np.array(payload2['entropy'])
    
    # Cosine similarity
    dot_product = np.dot(entropy1, entropy2)
    norm1 = np.linalg.norm(entropy1)
    norm2 = np.linalg.norm(entropy2)
    
    similarity = dot_product / (norm1 * norm2)
    return similarity

# Example
text1 = "The quick brown fox"
text2 = "The quick brown dog"
text3 = "Completely different text"

sim_1_2 = calculate_similarity(text1, text2)
sim_1_3 = calculate_similarity(text1, text3)

print(f"Similarity (text1, text2): {sim_1_2:.4f}")  # Should be high
print(f"Similarity (text1, text3): {sim_1_3:.4f}")  # Should be lower
```

---

## Encryption & Decryption

### Basic Encryption

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe,
    frackture_encrypt_payload,
    frackture_decrypt_payload
)

# Prepare data
sensitive_data = {"user": "alice", "balance": 1000, "ssn": "123-45-6789"}

# Create payload
preprocessed = frackture_preprocess_universal_v2_6(sensitive_data)
payload = frackture_v3_3_safe(preprocessed)

# Encrypt
encryption_key = "super-secret-key-2024"
encrypted = frackture_encrypt_payload(payload, encryption_key)

print(f"Encrypted payload keys: {encrypted.keys()}")
print(f"Signature: {encrypted['signature'][:32]}...")
print(f"Key ID: {encrypted['metadata']['key_id']}")

# Decrypt
try:
    decrypted = frackture_decrypt_payload(encrypted, encryption_key)
    print("Decryption successful!")
except ValueError as e:
    print(f"Decryption failed: {e}")
```

### Secure Message Transmission

```python
import json
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe,
    frackture_encrypt_payload,
    frackture_decrypt_payload
)

class SecureMessenger:
    def __init__(self, encryption_key):
        self.key = encryption_key
    
    def send_message(self, message):
        """Encrypt message for transmission"""
        # Preprocess and compress
        preprocessed = frackture_preprocess_universal_v2_6(message)
        payload = frackture_v3_3_safe(preprocessed)
        
        # Encrypt
        encrypted = frackture_encrypt_payload(payload, self.key)
        
        # Serialize for transmission
        return json.dumps(encrypted)
    
    def receive_message(self, encrypted_json):
        """Decrypt received message"""
        # Deserialize
        encrypted = json.loads(encrypted_json)
        
        # Decrypt
        try:
            payload = frackture_decrypt_payload(encrypted, self.key)
            return {
                'success': True,
                'payload': payload
            }
        except ValueError as e:
            return {
                'success': False,
                'error': str(e)
            }

# Example usage
messenger = SecureMessenger("shared-secret-key")

# Sender
message = "This is a secure message"
encrypted_msg = messenger.send_message(message)
print(f"Encrypted message size: {len(encrypted_msg)} bytes")

# Receiver
result = messenger.receive_message(encrypted_msg)
if result['success']:
    print(f"Message received successfully!")
    print(f"Payload: {result['payload']}")
else:
    print(f"Decryption error: {result['error']}")
```

### Multi-Key System

```python
import secrets
import hashlib
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe,
    frackture_encrypt_payload,
    frackture_decrypt_payload
)

class KeyManager:
    def __init__(self):
        self.keys = {}  # key_id -> key
    
    def generate_key(self, name):
        """Generate a new key"""
        key = secrets.token_urlsafe(32)
        key_id = hashlib.sha256(key.encode()).hexdigest()[:8]
        self.keys[key_id] = {'key': key, 'name': name}
        return key, key_id
    
    def get_key(self, key_id):
        """Retrieve key by ID"""
        return self.keys.get(key_id, {}).get('key')
    
    def encrypt(self, data, key_id):
        """Encrypt with specific key"""
        key = self.get_key(key_id)
        if not key:
            raise ValueError(f"Key {key_id} not found")
        
        preprocessed = frackture_preprocess_universal_v2_6(data)
        payload = frackture_v3_3_safe(preprocessed)
        return frackture_encrypt_payload(payload, key)
    
    def decrypt(self, encrypted):
        """Decrypt using key from metadata"""
        key_id = encrypted['metadata']['key_id']
        key = self.get_key(key_id)
        if not key:
            raise ValueError(f"Key {key_id} not found")
        
        return frackture_decrypt_payload(encrypted, key)

# Example usage
km = KeyManager()

# Generate keys for different purposes
user_key, user_key_id = km.generate_key("user_data")
admin_key, admin_key_id = km.generate_key("admin_data")

# Encrypt with different keys
user_data = "User information"
admin_data = "Administrative data"

encrypted_user = km.encrypt(user_data, user_key_id)
encrypted_admin = km.encrypt(admin_data, admin_key_id)

# Decrypt automatically selects correct key
decrypted_user = km.decrypt(encrypted_user)
decrypted_admin = km.decrypt(encrypted_admin)

print(f"User key ID: {user_key_id}")
print(f"Admin key ID: {admin_key_id}")
```

### Tamper Detection

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe,
    frackture_encrypt_payload,
    frackture_decrypt_payload
)

# Create and encrypt payload
data = "Critical system data"
preprocessed = frackture_preprocess_universal_v2_6(data)
payload = frackture_v3_3_safe(preprocessed)
encrypted = frackture_encrypt_payload(payload, "secret-key")

print("Original encryption successful")

# Simulate tampering
print("\nAttempting to tamper with data...")
encrypted_tampered = encrypted.copy()
encrypted_tampered["data"]["symbolic"] = "TAMPERED_DATA_HERE"

# Try to decrypt tampered data
try:
    frackture_decrypt_payload(encrypted_tampered, "secret-key")
    print("ERROR: Tampering not detected!")
except ValueError as e:
    print(f"✓ Tampering detected: {e}")

# Try with wrong key
print("\nAttempting decryption with wrong key...")
try:
    frackture_decrypt_payload(encrypted, "wrong-key")
    print("ERROR: Wrong key accepted!")
except ValueError as e:
    print(f"✓ Wrong key rejected: {e}")
```

---

## Hashing & Integrity

### Basic Hashing

```python
from frackture import frackture_deterministic_hash

# Simple hashing
data = "Important data to hash"
hash1 = frackture_deterministic_hash(data)
hash2 = frackture_deterministic_hash(data)

print(f"Hash 1: {hash1}")
print(f"Hash 2: {hash2}")
print(f"Hashes match: {hash1 == hash2}")

# Different data
different_data = "Different data"
hash3 = frackture_deterministic_hash(different_data)
print(f"Hash 3: {hash3}")
print(f"Hash 3 different: {hash1 != hash3}")
```

### Salted Hashing

```python
from frackture import frackture_deterministic_hash

def user_specific_hash(user_id, data):
    """Create user-specific hash with salt"""
    return frackture_deterministic_hash(data, salt=user_id)

# Same data, different users
data = "shared data"
hash_user1 = user_specific_hash("user_001", data)
hash_user2 = user_specific_hash("user_002", data)

print(f"User 1 hash: {hash_user1[:32]}...")
print(f"User 2 hash: {hash_user2[:32]}...")
print(f"Hashes different: {hash_user1 != hash_user2}")
```

### Integrity Checking

```python
from frackture import frackture_deterministic_hash
import time

class IntegrityChecker:
    def __init__(self):
        self.checksums = {}
    
    def store_checksum(self, data_id, data):
        """Store integrity checksum"""
        checksum = frackture_deterministic_hash(str(data))
        self.checksums[data_id] = {
            'checksum': checksum,
            'timestamp': time.time()
        }
        print(f"Stored checksum for {data_id}")
    
    def verify_integrity(self, data_id, data):
        """Verify data hasn't been modified"""
        if data_id not in self.checksums:
            return {'verified': False, 'error': 'No checksum found'}
        
        expected = self.checksums[data_id]['checksum']
        actual = frackture_deterministic_hash(str(data))
        
        verified = (expected == actual)
        
        return {
            'verified': verified,
            'data_id': data_id,
            'timestamp': self.checksums[data_id]['timestamp']
        }

# Example usage
checker = IntegrityChecker()

# Store original data
config = {"database": "localhost", "port": 5432}
checker.store_checksum("config", config)

# Verify unchanged
result = checker.verify_integrity("config", config)
print(f"Integrity check: {result['verified']}")  # True

# Verify after modification
config["port"] = 3306
result = checker.verify_integrity("config", config)
print(f"Integrity check after modification: {result['verified']}")  # False
```

### Content-Addressable Storage

```python
from frackture import frackture_deterministic_hash
import json

class ContentAddressableStore:
    def __init__(self):
        self.storage = {}
    
    def put(self, data):
        """Store data and return content hash"""
        # Generate content-based address
        address = frackture_deterministic_hash(json.dumps(data, sort_keys=True))
        
        # Store data at address
        self.storage[address] = data
        
        print(f"Stored at: {address[:16]}...")
        return address
    
    def get(self, address):
        """Retrieve data by content hash"""
        data = self.storage.get(address)
        
        if data is None:
            return None
        
        # Verify integrity
        expected_address = frackture_deterministic_hash(
            json.dumps(data, sort_keys=True)
        )
        
        if address != expected_address:
            raise ValueError("Data corruption detected!")
        
        return data
    
    def exists(self, address):
        """Check if content exists"""
        return address in self.storage

# Example usage
store = ContentAddressableStore()

# Store data
doc1 = {"title": "Document 1", "content": "Lorem ipsum"}
doc2 = {"title": "Document 2", "content": "Dolor sit amet"}

addr1 = store.put(doc1)
addr2 = store.put(doc2)

# Retrieve by address
retrieved = store.get(addr1)
print(f"Retrieved: {retrieved}")

# Deduplication: same content = same address
doc1_copy = {"title": "Document 1", "content": "Lorem ipsum"}
addr1_copy = store.put(doc1_copy)
print(f"Addresses match: {addr1 == addr1_copy}")  # True
```

---

## Self-Optimization

### Basic Optimization

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    optimize_frackture,
    frackture_v3_3_safe,
    frackture_v3_3_reconstruct
)
import numpy as np

# Prepare data
data = "Important data that needs optimal compression"
preprocessed = frackture_preprocess_universal_v2_6(data)

# Standard compression
standard_payload = frackture_v3_3_safe(preprocessed)
standard_recon = frackture_v3_3_reconstruct(standard_payload)
standard_mse = np.mean((preprocessed - standard_recon) ** 2)

# Optimized compression
optimized_payload, optimized_mse = optimize_frackture(preprocessed, num_trials=5)

print(f"Standard MSE: {standard_mse:.6f}")
print(f"Optimized MSE: {optimized_mse:.6f}")
print(f"Improvement: {(1 - optimized_mse/standard_mse) * 100:.2f}%")
```

### Batch Optimization

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    optimize_frackture
)

def optimize_batch(data_items, num_trials=5):
    """Optimize multiple items and return best payloads"""
    results = []
    
    for i, data in enumerate(data_items):
        preprocessed = frackture_preprocess_universal_v2_6(data)
        payload, mse = optimize_frackture(preprocessed, num_trials)
        
        results.append({
            'index': i,
            'payload': payload,
            'mse': mse
        })
        
        print(f"Item {i}: MSE = {mse:.6f}")
    
    return results

# Example
documents = [
    "First document content",
    "Second document with different content",
    "Third document about something else"
]

optimized_results = optimize_batch(documents, num_trials=7)

# Find best and worst
best = min(optimized_results, key=lambda x: x['mse'])
worst = max(optimized_results, key=lambda x: x['mse'])

print(f"\nBest MSE: {best['mse']:.6f} (document {best['index']})")
print(f"Worst MSE: {worst['mse']:.6f} (document {worst['index']})")
```

### Adaptive Optimization

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    optimize_frackture,
    frackture_v3_3_safe
)

class AdaptiveCompressor:
    def __init__(self, mse_threshold=0.05):
        self.mse_threshold = mse_threshold
        self.stats = {'optimized': 0, 'standard': 0}
    
    def compress(self, data):
        """Compress with adaptive optimization"""
        preprocessed = frackture_preprocess_universal_v2_6(data)
        
        # Try standard first (fast)
        standard_payload = frackture_v3_3_safe(preprocessed)
        
        # Quick MSE estimate
        from frackture import frackture_v3_3_reconstruct
        import numpy as np
        recon = frackture_v3_3_reconstruct(standard_payload)
        quick_mse = np.mean((preprocessed - recon) ** 2)
        
        # Optimize only if needed
        if quick_mse > self.mse_threshold:
            print(f"MSE {quick_mse:.4f} > threshold, optimizing...")
            payload, mse = optimize_frackture(preprocessed, num_trials=5)
            self.stats['optimized'] += 1
            return payload, mse, 'optimized'
        else:
            print(f"MSE {quick_mse:.4f} acceptable, using standard")
            self.stats['standard'] += 1
            return standard_payload, quick_mse, 'standard'
    
    def get_stats(self):
        total = self.stats['optimized'] + self.stats['standard']
        return {
            'optimized': self.stats['optimized'],
            'standard': self.stats['standard'],
            'optimization_rate': self.stats['optimized'] / total if total > 0 else 0
        }

# Example usage
compressor = AdaptiveCompressor(mse_threshold=0.05)

data_items = [
    "Simple short text",  # Likely good MSE
    "x" * 1000,  # Repetitive, likely good MSE
    "".join(chr(i % 256) for i in range(1000))  # Complex, may need optimization
]

for i, data in enumerate(data_items):
    print(f"\nCompressing item {i}...")
    payload, mse, method = compressor.compress(data)
    print(f"Method: {method}, MSE: {mse:.6f}")

print(f"\nStats: {compressor.get_stats()}")
```

---

## Advanced Patterns

### Pipeline Processing

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe,
    frackture_encrypt_payload,
    frackture_deterministic_hash
)

class FracturePipeline:
    def __init__(self, encryption_key=None):
        self.key = encryption_key
        self.results = []
    
    def process(self, data):
        """Full pipeline: preprocess -> compress -> encrypt -> hash"""
        # Step 1: Preprocess
        preprocessed = frackture_preprocess_universal_v2_6(data)
        
        # Step 2: Compress
        payload = frackture_v3_3_safe(preprocessed)
        
        # Step 3: Encrypt (if key provided)
        if self.key:
            encrypted = frackture_encrypt_payload(payload, self.key)
        else:
            encrypted = payload
        
        # Step 4: Generate hash for indexing
        import json
        hash_value = frackture_deterministic_hash(
            json.dumps(encrypted, sort_keys=True)
        )
        
        result = {
            'original_type': type(data).__name__,
            'payload': encrypted,
            'hash': hash_value,
            'encrypted': self.key is not None
        }
        
        self.results.append(result)
        return result
    
    def process_batch(self, data_items):
        """Process multiple items"""
        return [self.process(item) for item in data_items]

# Example usage
pipeline = FracturePipeline(encryption_key="my-secret-key")

data_items = [
    "Text data",
    {"key": "value"},
    b"binary data",
    [1, 2, 3, 4, 5]
]

results = pipeline.process_batch(data_items)

for i, result in enumerate(results):
    print(f"Item {i}:")
    print(f"  Type: {result['original_type']}")
    print(f"  Hash: {result['hash'][:32]}...")
    print(f"  Encrypted: {result['encrypted']}")
```

### Caching System

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe,
    frackture_deterministic_hash
)
import time

class FractureCache:
    def __init__(self, max_size=100):
        self.cache = {}
        self.max_size = max_size
        self.hits = 0
        self.misses = 0
    
    def _get_key(self, data):
        """Generate cache key from data"""
        return frackture_deterministic_hash(str(data))
    
    def get_or_compute(self, data):
        """Get from cache or compute"""
        cache_key = self._get_key(data)
        
        if cache_key in self.cache:
            self.hits += 1
            return self.cache[cache_key], True
        
        # Cache miss, compute
        self.misses += 1
        preprocessed = frackture_preprocess_universal_v2_6(data)
        payload = frackture_v3_3_safe(preprocessed)
        
        # Store in cache
        if len(self.cache) >= self.max_size:
            # Simple eviction: remove oldest
            oldest = min(self.cache.items(), 
                        key=lambda x: x[1]['timestamp'])
            del self.cache[oldest[0]]
        
        self.cache[cache_key] = {
            'payload': payload,
            'timestamp': time.time()
        }
        
        return payload, False
    
    def stats(self):
        total = self.hits + self.misses
        hit_rate = self.hits / total if total > 0 else 0
        return {
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': hit_rate,
            'cache_size': len(self.cache)
        }

# Example usage
cache = FractureCache(max_size=10)

# Process some data
data_items = ["item1", "item2", "item1", "item3", "item1"]

for data in data_items:
    payload, from_cache = cache.get_or_compute(data)
    print(f"Data: {data}, From cache: {from_cache}")

print(f"\nCache stats: {cache.stats()}")
```

### Streaming Processing

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe
)
import json

class StreamingProcessor:
    def __init__(self, output_file):
        self.output_file = output_file
        self.processed_count = 0
    
    def process_stream(self, data_generator):
        """Process data stream and write results"""
        with open(self.output_file, 'w') as f:
            for data in data_generator:
                # Process each item
                preprocessed = frackture_preprocess_universal_v2_6(data)
                payload = frackture_v3_3_safe(preprocessed)
                
                # Write to file immediately (streaming)
                result = {
                    'index': self.processed_count,
                    'symbolic': payload['symbolic'],
                    'entropy': payload['entropy']
                }
                f.write(json.dumps(result) + '\n')
                f.flush()  # Ensure written
                
                self.processed_count += 1
                
                if self.processed_count % 100 == 0:
                    print(f"Processed {self.processed_count} items...")
        
        print(f"Total processed: {self.processed_count}")

# Example usage
def data_generator():
    """Simulate streaming data source"""
    for i in range(1000):
        yield f"Data item {i}: " + "x" * (i % 100)

processor = StreamingProcessor("output_stream.jsonl")
processor.process_stream(data_generator())
```

---

## Integration Examples

### Flask Web API

```python
from flask import Flask, request, jsonify
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe,
    frackture_encrypt_payload,
    frackture_decrypt_payload
)

app = Flask(__name__)
ENCRYPTION_KEY = "your-secret-key-here"

@app.route('/api/compress', methods=['POST'])
def compress_data():
    """Compress and return fingerprint"""
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        preprocessed = frackture_preprocess_universal_v2_6(data)
        payload = frackture_v3_3_safe(preprocessed)
        
        return jsonify({
            'success': True,
            'fingerprint': payload['symbolic'][:32],
            'payload_size': len(payload['symbolic']) + len(payload['entropy']) * 8
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/encrypt', methods=['POST'])
def encrypt_data():
    """Compress and encrypt data"""
    try:
        data = request.json.get('data')
        key = request.json.get('key', ENCRYPTION_KEY)
        
        preprocessed = frackture_preprocess_universal_v2_6(data)
        payload = frackture_v3_3_safe(preprocessed)
        encrypted = frackture_encrypt_payload(payload, key)
        
        return jsonify({
            'success': True,
            'encrypted_payload': encrypted
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/decrypt', methods=['POST'])
def decrypt_data():
    """Decrypt payload"""
    try:
        encrypted = request.json.get('encrypted_payload')
        key = request.json.get('key', ENCRYPTION_KEY)
        
        payload = frackture_decrypt_payload(encrypted, key)
        
        return jsonify({
            'success': True,
            'payload': payload
        })
    except ValueError as e:
        return jsonify({'error': f'Decryption failed: {e}'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Database Storage

```python
import sqlite3
import json
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe,
    frackture_encrypt_payload,
    frackture_deterministic_hash
)

class FractureDB:
    def __init__(self, db_path, encryption_key=None):
        self.conn = sqlite3.connect(db_path)
        self.key = encryption_key
        self._create_tables()
    
    def _create_tables(self):
        """Create database schema"""
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS fingerprints (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fingerprint TEXT UNIQUE NOT NULL,
                payload_json TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def store(self, data):
        """Store data fingerprint"""
        # Compress
        preprocessed = frackture_preprocess_universal_v2_6(data)
        payload = frackture_v3_3_safe(preprocessed)
        
        # Optionally encrypt
        if self.key:
            payload = frackture_encrypt_payload(payload, self.key)
        
        # Generate fingerprint for indexing
        fingerprint = payload.get('symbolic', 
                                 frackture_deterministic_hash(json.dumps(payload)))
        
        # Store
        try:
            self.conn.execute(
                'INSERT INTO fingerprints (fingerprint, payload_json) VALUES (?, ?)',
                (fingerprint, json.dumps(payload))
            )
            self.conn.commit()
            return fingerprint
        except sqlite3.IntegrityError:
            return None  # Duplicate
    
    def retrieve(self, fingerprint):
        """Retrieve by fingerprint"""
        cursor = self.conn.execute(
            'SELECT payload_json FROM fingerprints WHERE fingerprint = ?',
            (fingerprint,)
        )
        row = cursor.fetchone()
        
        if row:
            return json.loads(row[0])
        return None
    
    def close(self):
        self.conn.close()

# Example usage
db = FractureDB('fingerprints.db', encryption_key='db-key')

# Store data
data1 = "Important document"
fp1 = db.store(data1)
print(f"Stored with fingerprint: {fp1[:32]}...")

# Retrieve
payload = db.retrieve(fp1)
print(f"Retrieved: {payload['symbolic'][:32]}...")

db.close()
```

---

## Error Handling

### Robust Decryption

```python
from frackture import (
    frackture_decrypt_payload,
    frackture_v3_3_reconstruct
)
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def safe_decrypt(encrypted_payload, key, max_retries=3):
    """Decrypt with error handling and retries"""
    for attempt in range(max_retries):
        try:
            payload = frackture_decrypt_payload(encrypted_payload, key)
            logger.info(f"Decryption successful on attempt {attempt + 1}")
            return {'success': True, 'payload': payload}
        
        except ValueError as e:
            logger.warning(f"Decryption attempt {attempt + 1} failed: {e}")
            
            if "Invalid key" in str(e):
                # Wrong key, no point retrying
                return {
                    'success': False,
                    'error': 'Authentication failed',
                    'recoverable': False
                }
            elif "corrupted" in str(e).lower():
                # Possible network issue, retry
                if attempt < max_retries - 1:
                    continue
                return {
                    'success': False,
                    'error': 'Data corrupted',
                    'recoverable': True
                }
        
        except Exception as e:
            logger.error(f"Unexpected error: {e}", exc_info=True)
            return {
                'success': False,
                'error': f'Unexpected error: {e}',
                'recoverable': False
            }
    
    return {
        'success': False,
        'error': 'Max retries exceeded',
        'recoverable': True
    }

# Example usage
encrypted = {'data': {...}, 'signature': '...', 'metadata': {...}}
result = safe_decrypt(encrypted, "my-key")

if result['success']:
    print(f"Payload: {result['payload']}")
else:
    print(f"Error: {result['error']}")
    if result['recoverable']:
        print("Error may be recoverable, consider retry")
```

### Validation Wrapper

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe,
    frackture_v3_3_reconstruct
)
import numpy as np

def validate_and_compress(data, mse_threshold=0.1):
    """Compress with validation"""
    try:
        # Validate input
        if data is None:
            raise ValueError("Data cannot be None")
        
        if isinstance(data, str) and len(data) == 0:
            raise ValueError("Data cannot be empty string")
        
        # Preprocess
        preprocessed = frackture_preprocess_universal_v2_6(data)
        
        # Validate preprocessed vector
        if not isinstance(preprocessed, np.ndarray):
            raise TypeError("Preprocessing failed to produce numpy array")
        
        if len(preprocessed) != 768:
            raise ValueError(f"Expected 768 elements, got {len(preprocessed)}")
        
        # Compress
        payload = frackture_v3_3_safe(preprocessed)
        
        # Validate payload structure
        if 'symbolic' not in payload or 'entropy' not in payload:
            raise ValueError("Invalid payload structure")
        
        if len(payload['symbolic']) != 64:
            raise ValueError(f"Expected 64-char symbolic, got {len(payload['symbolic'])}")
        
        if len(payload['entropy']) != 16:
            raise ValueError(f"Expected 16 entropy features, got {len(payload['entropy'])}")
        
        # Validate reconstruction quality
        reconstructed = frackture_v3_3_reconstruct(payload)
        mse = np.mean((preprocessed - reconstructed) ** 2)
        
        if mse > mse_threshold:
            return {
                'success': False,
                'error': f'MSE {mse:.4f} exceeds threshold {mse_threshold}',
                'mse': mse,
                'payload': payload
            }
        
        return {
            'success': True,
            'payload': payload,
            'mse': mse
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'type': type(e).__name__
        }

# Example usage
test_data = ["Valid data", "", None, {"key": "value"}]

for data in test_data:
    result = validate_and_compress(data)
    print(f"Data: {data}")
    print(f"Result: {result['success']}")
    if not result['success']:
        print(f"Error: {result['error']}")
    print()
```

---

## Performance Tips

### Batch Processing

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe
)
import time

def process_batch_efficient(data_items):
    """Process items efficiently"""
    results = []
    start_time = time.time()
    
    for i, data in enumerate(data_items):
        preprocessed = frackture_preprocess_universal_v2_6(data)
        payload = frackture_v3_3_safe(preprocessed)
        results.append(payload)
        
        if (i + 1) % 100 == 0:
            elapsed = time.time() - start_time
            rate = (i + 1) / elapsed
            print(f"Processed {i + 1} items ({rate:.1f} items/sec)")
    
    total_time = time.time() - start_time
    print(f"\nTotal: {len(data_items)} items in {total_time:.2f}s")
    print(f"Average: {len(data_items) / total_time:.1f} items/sec")
    
    return results

# Example
large_dataset = [f"Item {i}" for i in range(1000)]
results = process_batch_efficient(large_dataset)
```

---

**Next Steps:**
- Read [ARCHITECTURE.md](./ARCHITECTURE.md) for implementation details
- See [SECURITY.md](./SECURITY.md) for security best practices
- Check [FAQ.md](./FAQ.md) for common questions
