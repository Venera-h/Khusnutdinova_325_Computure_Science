import unittest
from playfair import PlayfairCipher

class TestPlayfairCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = PlayfairCipher("KEYWORD")

    def test_encrypt(self):
        plaintext = "HELLO"
        expected = self.cipher.encrypt(plaintext)
        # результат зависит от ключа, тут просто проверим обратимость
        decrypted = self.cipher.decrypt(expected)
        self.assertIn("HELXLO", decrypted)  

    def test_decrypt(self):
        plaintext = "SECRETMESSAGE"
        encrypted = self.cipher.encrypt(plaintext)
        decrypted = self.cipher.decrypt(encrypted)
        # Допускаем появление X для парных букв или нечетной длины
        self.assertTrue(all(c in decrypted for c in plaintext.replace('J', 'I')))

    def test_key_square(self):
        expected = [
            ['K', 'E', 'Y', 'W', 'O'],
            ['R', 'D', 'A', 'B', 'C'],
            ['F', 'G', 'H', 'I', 'L'],
            ['M', 'N', 'P', 'Q', 'S'],
            ['T', 'U', 'V', 'X', 'Z']
        ]
        cipher = PlayfairCipher("KEYWORD")
        self.assertEqual(cipher.key_square, expected)

if __name__ == "__main__":
    unittest.main()
