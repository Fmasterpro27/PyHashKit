import hashlib

def hash_text(text: str, algorithm: str = "sha256") -> str:
    try:
        hash_obj = hashlib.new(algorithm)
    except ValueError:
        raise ValueError(
            f"Unsupported algorithm: {algorithm}"
        )

    hash_obj.update(text.encode("utf-8"))
    return hash_obj.hexdigest()



def hash_file(file_path: str, algorithm: str = "sha256") -> str:
    try:
        hash_obj = hashlib.new(algorithm)
    except ValueError:
        raise ValueError(
            f"Unsupported algorithm: {algorithm}"
        )

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hash_obj.update(chunk)

    return hash_obj.hexdigest()