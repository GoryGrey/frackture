#!/usr/bin/env python3
"""
Generate redistribution-safe sample datasets for benchmarking.
All samples are small base files that will be scaled up during benchmarking.
"""

import json
import csv
import sqlite3
import pickle
import os
from pathlib import Path

# Create output directory
output_dir = Path(__file__).parent
output_dir.mkdir(exist_ok=True)

print("Generating sample datasets...")

# ========== TEXT DATASETS ==========

# Plain text (prose/documentation)
plain_text = """The quick brown fox jumps over the lazy dog. This is sample text content
that represents typical prose, documentation, or natural language content.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

This text can be repeated and concatenated to create larger test files.
It contains standard ASCII characters and common punctuation marks.
The content is designed to be representative of real-world text documents.
"""

with open(output_dir / "sample_text.txt", "w") as f:
    f.write(plain_text)
print("✓ Created sample_text.txt")

# Log file format
log_content = """2024-01-15 10:23:45.123 INFO [main] Application started successfully
2024-01-15 10:23:45.456 DEBUG [worker-1] Processing request id=12345
2024-01-15 10:23:45.789 DEBUG [worker-2] Cache hit for key: user_profile_6789
2024-01-15 10:23:46.012 WARN [db-pool] Connection pool utilization at 85%
2024-01-15 10:23:46.345 ERROR [api] HTTP 500 - Internal server error at /api/users/update
2024-01-15 10:23:46.678 INFO [metrics] Request latency: 234ms, throughput: 1250 req/s
2024-01-15 10:23:46.901 DEBUG [cache] Evicted 50 entries from LRU cache
2024-01-15 10:23:47.234 INFO [scheduler] Cron job 'cleanup-old-logs' completed in 2.3s
"""

with open(output_dir / "sample_log.log", "w") as f:
    f.write(log_content)
print("✓ Created sample_log.log")

# JSON structured data
json_data = {
    "users": [
        {"id": 1, "name": "Alice Smith", "email": "alice@example.com", "age": 28, "active": True, "tags": ["python", "rust"]},
        {"id": 2, "name": "Bob Johnson", "email": "bob@example.com", "age": 35, "active": False, "tags": ["javascript", "go"]},
        {"id": 3, "name": "Carol White", "email": "carol@example.com", "age": 42, "active": True, "tags": ["java", "kotlin"]},
    ],
    "metadata": {
        "version": "2.0",
        "timestamp": "2024-01-15T10:23:45Z",
        "count": 3,
        "schema": "user_v2"
    },
    "settings": {
        "enable_caching": True,
        "max_connections": 100,
        "timeout_seconds": 30
    }
}

with open(output_dir / "sample_data.json", "w") as f:
    json.dump(json_data, f, indent=2)
print("✓ Created sample_data.json")

# CSV data
csv_data = [
    ["id", "product", "category", "price", "quantity", "sold"],
    [1, "Laptop", "Electronics", 999.99, 50, 32],
    [2, "Mouse", "Peripherals", 29.99, 200, 156],
    [3, "Keyboard", "Peripherals", 79.99, 150, 98],
    [4, "Monitor", "Electronics", 299.99, 75, 45],
    [5, "USB Cable", "Accessories", 9.99, 500, 387],
]

with open(output_dir / "sample_data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)
print("✓ Created sample_data.csv")

# ========== BINARY DATASETS ==========

# Minimal PNG (1x1 red pixel)
png_data = (
    b'\x89PNG\r\n\x1a\n'  # PNG signature
    b'\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde'  # IHDR chunk
    b'\x00\x00\x00\x0cIDATx\x9cc\xf8\xcf\xc0\x00\x00\x00\x03\x00\x01\x8f\xb3\x8f='  # IDAT chunk
    b'\x00\x00\x00\x00IEND\xaeB`\x82'  # IEND chunk
)

with open(output_dir / "sample_image.png", "wb") as f:
    f.write(png_data)
print("✓ Created sample_image.png")

# Minimal JPEG (tiny valid JPEG)
jpeg_data = (
    b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00'
    b'\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c'
    b'\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c'
    b'\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342'
    b'\xff\xc0\x00\x0b\x08\x00\x01\x00\x01\x01\x01\x11\x00'
    b'\xff\xc4\x00\x14\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\xff\xda\x00\x08\x01\x01\x00\x00?\x00\x7f\x00\xff\xd9'
)

with open(output_dir / "sample_image.jpg", "wb") as f:
    f.write(jpeg_data)
print("✓ Created sample_image.jpg")

# Minimal PDF
pdf_data = b"""%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
>>
endobj
2 0 obj
<<
/Type /Pages
/Kids [3 0 R]
/Count 1
>>
endobj
3 0 obj
<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 612 792]
/Contents 4 0 R
>>
endobj
4 0 obj
<<
/Length 44
>>
stream
BT
/F1 12 Tf
100 700 Td
(Sample PDF) Tj
ET
endstream
endobj
xref
0 5
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000214 00000 n 
trailer
<<
/Size 5
/Root 1 0 R
>>
startxref
307
%%EOF
"""

with open(output_dir / "sample_document.pdf", "wb") as f:
    f.write(pdf_data)
print("✓ Created sample_document.pdf")

# Minimal GIF (1x1 transparent pixel)
gif_data = (
    b'GIF89a'  # Header
    b'\x01\x00\x01\x00'  # Logical Screen Descriptor: 1x1
    b'\x80\x00\x00'  # Global Color Table Flag
    b'\x00\x00\x00\xff\xff\xff'  # Global Color Table
    b'\x21\xf9\x04\x01\x00\x00\x00\x00'  # Graphic Control Extension
    b'\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00'  # Image Descriptor
    b'\x02\x02\x44\x01\x00'  # Image Data
    b'\x3b'  # Trailer
)

with open(output_dir / "sample_animation.gif", "wb") as f:
    f.write(gif_data)
print("✓ Created sample_animation.gif")

# ========== STRUCTURED DATASETS ==========

# SQLite database
db_path = output_dir / "sample_database.db"
if db_path.exists():
    os.remove(db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

cursor.execute('''
    CREATE TABLE posts (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        title TEXT NOT NULL,
        content TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

cursor.executemany(
    'INSERT INTO users (username, email) VALUES (?, ?)',
    [
        ('alice', 'alice@example.com'),
        ('bob', 'bob@example.com'),
        ('carol', 'carol@example.com'),
    ]
)

cursor.executemany(
    'INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)',
    [
        (1, 'First Post', 'This is the content of the first post'),
        (2, 'Second Post', 'Another interesting post with more content'),
        (1, 'Third Post', 'Yet another post from Alice'),
    ]
)

conn.commit()
conn.close()
print("✓ Created sample_database.db")

# Pickled Python object
pickled_data = {
    'users': [
        {'id': 1, 'name': 'Alice', 'scores': [95, 87, 92]},
        {'id': 2, 'name': 'Bob', 'scores': [78, 85, 90]},
    ],
    'metadata': {
        'version': 1,
        'format': 'pickle',
    },
    'numpy_array': None,  # Would include numpy array if available
}

with open(output_dir / "sample_pickle.pkl", "wb") as f:
    pickle.dump(pickled_data, f)
print("✓ Created sample_pickle.pkl")

# MessagePack (if available, else skip)
try:
    import msgpack
    
    msgpack_data = {
        'users': [
            {'id': 1, 'name': 'Alice', 'active': True},
            {'id': 2, 'name': 'Bob', 'active': False},
        ],
        'settings': {
            'timeout': 30,
            'retries': 3,
        }
    }
    
    with open(output_dir / "sample_msgpack.msgpack", "wb") as f:
        msgpack.pack(msgpack_data, f)
    print("✓ Created sample_msgpack.msgpack")
except ImportError:
    print("⚠ Skipped sample_msgpack.msgpack (msgpack not installed)")

# ========== CODE DATASETS ==========

# JavaScript code
js_code = """// Sample JavaScript module
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

class DataProcessor {
    constructor(options) {
        this.options = options || {};
        this.cache = new Map();
    }
    
    process(data) {
        if (this.cache.has(data)) {
            return this.cache.get(data);
        }
        
        const result = data.map(item => item * 2).filter(x => x > 10);
        this.cache.set(data, result);
        return result;
    }
}

module.exports = { fibonacci, DataProcessor };
"""

with open(output_dir / "sample_code.js", "w") as f:
    f.write(js_code)
print("✓ Created sample_code.js")

# Minified JavaScript
minified_js = "function f(n){return n<=1?n:f(n-1)+f(n-2)}class D{constructor(o){this.o=o||{};this.c=new Map()}p(d){if(this.c.has(d))return this.c.get(d);const r=d.map(i=>i*2).filter(x=>x>10);this.c.set(d,r);return r}}module.exports={f,D};"

with open(output_dir / "sample_minified.min.js", "w") as f:
    f.write(minified_js)
print("✓ Created sample_minified.min.js")

# Python module
python_code = '''"""Sample Python module for benchmarking"""

import math
from typing import List, Optional


def calculate_statistics(data: List[float]) -> dict:
    """Calculate basic statistics for a list of numbers."""
    if not data:
        return {}
    
    sorted_data = sorted(data)
    n = len(data)
    
    return {
        'mean': sum(data) / n,
        'median': sorted_data[n // 2],
        'min': sorted_data[0],
        'max': sorted_data[-1],
        'stddev': math.sqrt(sum((x - sum(data) / n) ** 2 for x in data) / n)
    }


class DataValidator:
    """Validate and sanitize input data."""
    
    def __init__(self, strict: bool = False):
        self.strict = strict
        self.errors: List[str] = []
    
    def validate_email(self, email: str) -> bool:
        """Validate email format."""
        if '@' not in email or '.' not in email.split('@')[-1]:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_positive(self, value: float) -> bool:
        """Ensure value is positive."""
        if value <= 0:
            self.errors.append(f"Value must be positive: {value}")
            return False
        return True
'''

with open(output_dir / "sample_module.py", "w") as f:
    f.write(python_code)
print("✓ Created sample_module.py")

# ========== MIXED PAYLOAD ==========

# Create a mixed binary payload combining different data types
mixed_payload = b""
mixed_payload += b"HEADER:MIXED_PAYLOAD\n"
mixed_payload += plain_text.encode('utf-8')
mixed_payload += b"\n---JSON_SECTION---\n"
mixed_payload += json.dumps(json_data).encode('utf-8')
mixed_payload += b"\n---BINARY_SECTION---\n"
mixed_payload += png_data
mixed_payload += b"\n---CODE_SECTION---\n"
mixed_payload += js_code.encode('utf-8')
mixed_payload += b"\n---END---\n"

with open(output_dir / "sample_mixed.bin", "wb") as f:
    f.write(mixed_payload)
print("✓ Created sample_mixed.bin")

print("\n✅ All sample datasets generated successfully!")
print(f"📁 Location: {output_dir}")
