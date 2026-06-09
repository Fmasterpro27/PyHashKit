# PyHashKit

> A lightweight Python library and CLI for hashing text and files using multiple cryptographic algorithms.

[![PyPI version](https://img.shields.io/pypi/v/pyhashkit.svg)](https://pypi.org/project/pyhashkit/)
[![Python versions](https://img.shields.io/pypi/pyversions/pyhashkit.svg)](https://pypi.org/project/pyhashkit/)
[![License](https://img.shields.io/pypi/l/pyhashkit.svg)](LICENSE)

---

## Features

- 🔐 Hash text strings
- 📄 Hash files of any size
- 💻 Built-in CLI support
- ⚡ Supports multiple algorithms
- 📦 Zero dependencies
- 🐍 Python 3.8+
- 🚀 Lightweight and fast

---

## Why PyHashKit?

PyHashKit provides a simple and beginner-friendly interface for Python's built-in hashing functionality.

Instead of manually working with `hashlib`, you can hash text and files with a single function call or directly from the command line.

---

## Supported Algorithms

PyHashKit supports most algorithms available through Python's built-in `hashlib`.

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

### Not Supported

The following algorithms are currently not supported:

- SHAKE-128 (`shake_128`)
- SHAKE-256 (`shake_256`)

These algorithms require a custom digest length and are intentionally excluded to keep the API simple and consistent.

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

# Command Line Interface (CLI)

PyHashKit includes a built-in command-line interface for hashing text and files directly from your terminal.

## Available Commands

```text
text         Hash a text string
file         Hash a file
commands     Show all commands
```

## Flags

```text
-v, -V, --version
             Show version information
```

## Options

```text
-a, --algorithm
             Specify hashing algorithm
             (default: sha256)
```

## Examples

Hash text:

```bash
pyhashkit text "Hello World"
```

Hash text using MD5:

```bash
pyhashkit text "Hello World" -a md5
```

Hash a file:

```bash
pyhashkit file example.txt
```

Hash a file using SHA-512:

```bash
pyhashkit file example.txt -a sha512
```

Show version information:

```bash
pyhashkit -v
```

Show all available commands:

```bash
pyhashkit commands
```

---

# Python API

## Hash Text

```python
from pyhashkit import hash_text

result = hash_text("Hello World")

print(result)
```

## Hash Text Using MD5

```python
from pyhashkit import hash_text

result = hash_text(
    "Hello World",
    algorithm="md5"
)

print(result)
```

## Hash File

```python
from pyhashkit import hash_file

result = hash_file("example.txt")

print(result)
```

## Hash File Using SHA-512

```python
from pyhashkit import hash_file

result = hash_file(
    "example.txt",
    algorithm="sha512"
)

print(result)
```

---

## Version Information

```python
from pyhashkit import __version__

print(__version__)
```

---

## Available Exports

```python
from pyhashkit import (
    hash_text,
    hash_file,
    algorithms,
    __version__
)
```

### algorithms

Returns a list of supported hashing algorithms available on the current Python installation.

```python
from pyhashkit import algorithms

print(algorithms())
```

---

## Example Output

```text
a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
```

---

## Project Structure

```text
PyHashKit/
├── pyhashkit/
│   ├── __init__.py
│   ├── hashing.py
│   ├── cli.py
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
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## Author

Developed by **JackMa**

GitHub:
https://github.com/Fmasterpro27

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
