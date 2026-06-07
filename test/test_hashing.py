import unittest
import os
import tempfile
from pyhashkit.hashing import hash_text, hash_file

class TestHashing(unittest.TestCase):
    def test_hash_text_default_sha256(self):
        text = "hello world"
        expected = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
        self.assertEqual(hash_text(text), expected)

    def test_hash_text_md5(self):
        text = "hello world"
        expected = "5eb63bbbe01eeed093cb22bb8f5acdc3"
        self.assertEqual(hash_text(text, algorithm="md5"), expected)

    def test_hash_text_invalid_algorithm(self):
        with self.assertRaises(ValueError):
            hash_text("test", algorithm="invalid_algo")

    def test_hash_file_sha256(self):
        content = b"file content"
        expected = "e0ac3601005dfa1864f5392aabaf7d898b1b5bab854f1acb4491bcd806b76b0c"
        
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(content)
            tmp_path = tmp.name
        
        try:
            self.assertEqual(hash_file(tmp_path), expected)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_hash_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            hash_file("non_existent_file.txt")

if __name__ == "__main__":
    unittest.main()
