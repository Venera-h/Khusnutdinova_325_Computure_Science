import unittest
from cesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):
    def test_lowercase(self):
        self.assertEqual(caesar_cipher("abc", 3), "def")

    def test_uppercase(self):
        self.assertEqual(caesar_cipher("ABC", 3), "DEF")

    def test_mixed_case(self):
        self.assertEqual(caesar_cipher("AbC", 3), "DeF")

    def test_non_alpha_characters(self):
        self.assertEqual(caesar_cipher("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_negative_shift(self):
        self.assertEqual(caesar_cipher("def", -3), "abc")

    def test_large_shift(self):
        self.assertEqual(caesar_cipher("abc", 29), "def")  # 29 % 26 = 3

if __name__ == "__main__":
    unittest.main()
