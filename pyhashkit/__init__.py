from .hashing import hash_text, hash_file, algorithms
from importlib.metadata import version

__version__ = version("PyHashKit")

__all__ = [
    "hash_text",
    "hash_file",
    "algorithms",
    "__version__"
]