import hashlib

def algorithms():
    return sorted(hashlib.algorithms_available)


def hash_text(text: str, algorithm: str = "sha256") -> str:
    if not isinstance(text, str):
        raise TypeError(
            "text must be a string"
        )

    try:
        hash_obj = hashlib.new(algorithm)
    except ValueError:
        raise ValueError(
            f"Unsupported algorithm: {algorithm}"
        )

    hash_obj.update(text.encode("utf-8"))
    return hash_obj.hexdigest()


def hash_file(file_path: str, algorithm: str = "sha256") -> str:
    if not isinstance(file_path, str):
        raise TypeError(
            "file_path must be a string"
        )

    try:
        hash_obj = hashlib.new(algorithm)
    except ValueError:
        raise ValueError(
            f"Unsupported algorithm: {algorithm}"
        )

    try:
        with open(file_path, "rb") as f:
            for chunk in iter(
                lambda: f.read(8192),
                b""
            ):
                hash_obj.update(chunk)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    except PermissionError:
        raise PermissionError(
            f"Permission denied: {file_path}"
        )

    except OSError as e:
        raise OSError(
            f"Failed to read file: {e}"
        )

    return hash_obj.hexdigest()