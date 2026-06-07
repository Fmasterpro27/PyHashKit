# PyHashKit

> A lightweight Python library for hashing text and files using multiple cryptographic algorithms.

[![PyPI version](https://img.shields.io/pypi/v/pyhashkit.svg)](https://pypi.org/project/pyhashkit/)
[![Python versions](https://img.shields.io/pypi/pyversions/pyhashkit.svg)](https://pypi.org/project/pyhashkit/)
[![License](https://img.shields.io/pypi/l/pyhashkit.svg)](LICENSE)

---

## Features

- 🔐 Hash text strings
- 📄 Hash files of any size
- ⚡ Supports multiple algorithms
- 📦 Zero dependencies
- 🐍 Python 3.8+
- 🚀 Lightweight and fast

---

## Supported Algorithms

PyHashKit supports any algorithm available through Python's built-in `hashlib`.

Common examples:

- SHA-256
- SHA-512
- SHA-224
- SHA-384
- MD5
- SHA-1
- SHA3-224
- SHA3-256
- SHA3-384
- SHA3-512
- BLAKE2b
- BLAKE2s

---

## Installation

```bash
pip install PyHashKit
```

---

## Quick Start

```python
from pyhashkit import hash_text, hash_file

print(hash_text("Hello World"))
print(hash_file("example.txt"))
```

---

## Python API

### Hash Text

```python
from pyhashkit import hash_text

result = hash_text("Hello World")

print(result)
```

### Hash Text Using MD5

```python
from pyhashkit import hash_text

result = hash_text(
    "Hello World",
    algorithm="md5"
)

print(result)
```

### Hash File

```python
from pyhashkit import hash_file

result = hash_file("example.txt")

print(result)
```

### Hash File Using SHA-512

```python
from pyhashkit import hash_file

result = hash_file(
    "example.txt",
    algorithm="sha512"
)

print(result)
```

---

## Example Output

```text
a591a6d40bf420404a011733cfb7b190
d62c65bf0bcda32b57b277d9ad9f146e
```

---

## Project Structure

```text
PyHashKit/
├── pyhashkit/
│   ├── __init__.py
│   ├── hashing.py
│   └── version.py
├── tests/
│   └── test_hashing.py
├── pyproject.toml
├── LICENSE
└── README.md
```

---

## Contributing

Contributions, bug reports, and feature requests are welcome.

1. Fork the repository
2. Create a branch
3. Make your changes
4. Submit a pull request

---

## Links

Homepage:
https://github.com/Fmasterpro27/PyHashKit

Issues:
https://github.com/Fmasterpro27/PyHashKit/issues

PyPI:
https://pypi.org/project/pyhashkit/

---

## License

Licensed under the Apache License 2.0.
