import unittest
from vigenere import vigenere_encrypt, vigenere_decrypt

class TestVigenereCipher(unittest.TestCase):
    def test_encrypt_decrypt(self):
        plain = "ATTACKATDAWN"
        key = "LEMON"
        cipher = vigenere_encrypt(plain, key)
        self.assertEqual(cipher, "LXFOPVEFRNHR")
        decrypted = vigenere_decrypt(cipher, key)
        self.assertEqual(decrypted, plain)

    def test_encrypt_decrypt_lowercase(self):
        plain = "attackatdawn"
        key = "lemon"
        cipher = vigenere_encrypt(plain, key)
        self.assertEqual(cipher, "lxfopvefrnhr")
        decrypted = vigenere_decrypt(cipher, key)
        self.assertEqual(decrypted, plain)

    def test_with_nonalpha(self):
        plain = "attack at dawn! 123"
        key = "lemon"
        cipher = vigenere_encrypt(plain, key)
        self.assertEqual(cipher, "lxfopv ef rnhr! 123")
        decrypted = vigenere_decrypt(cipher, key)
        self.assertEqual(decrypted, plain)

    def test_empty(self):
        self.assertEqual(vigenere_encrypt('', 'key'), '')
        self.assertEqual(vigenere_decrypt('', 'key'), '')

    def test_encrypt_decrypt_flower(self):
        plain = "HELLOWORLD"
        key = "FLOWER"
        cipher = vigenere_encrypt(plain, key)
        self.assertEqual(cipher, "MPPMYWQYYH")  
        decrypted = vigenere_decrypt(cipher, key)
        self.assertEqual(decrypted, plain)

if __name__ == '__main__':
    unittest.main()