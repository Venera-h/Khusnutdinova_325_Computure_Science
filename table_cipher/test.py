import unittest
from enhanced_table_cipher import encrypt, decrypt

class TestEnhancedTableCipher(unittest.TestCase):
    def test_encrypt_simple(self):
        self.assertEqual(encrypt("HELLO", "SECRET", 3), "KTOOU")

    def test_encrypt_with_non_alpha(self):
        self.assertEqual(encrypt("HELLO, WORLD!", "SECRET", 3), "KTOOU, ZUBOH!")

    def test_encrypt_large_shift(self):
        self.assertEqual(encrypt("HELLO", "SECRET", 29), "KTOOU")  # 29 % 26 = 3

    def test_decrypt_simple(self):
        self.assertEqual(decrypt("KTOOU", "SECRET", 3), "HELLO")

    def test_decrypt_with_non_alpha(self):
        self.assertEqual(decrypt("KTOOU, ZUBOH!", "SECRET", 3), "HELLO, WORLD!")

    def test_empty_string(self):
        self.assertEqual(encrypt("", "SECRET", 3), "")
        self.assertEqual(decrypt("", "SECRET", 3), "")

if __name__ == "__main__":
    unittest.main()
