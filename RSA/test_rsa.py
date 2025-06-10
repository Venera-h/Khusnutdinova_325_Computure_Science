import unittest
from rsa import RSA

class TestRSA(unittest.TestCase):
    def setUp(self):
        self.rsa = RSA()

    def test_encrypt_decrypt_str(self):
        msg = "Test123"
        encrypted = self.rsa.encrypt(msg)
        decrypted = self.rsa.decrypt(encrypted)
        self.assertEqual(decrypted, msg)

    def test_encrypt_decrypt_int(self):
        msg = 12345
        encrypted = self.rsa.encrypt(msg)
        decrypted = self.rsa.decrypt(encrypted)
        self.assertEqual(decrypted, msg)

    def test_message_too_large(self):
        n = self.rsa.n
        too_big = n + 1
        with self.assertRaises(ValueError):
            self.rsa.encrypt(too_big)

    def test_keys_valid(self):
        self.assertEqual((self.rsa.e * self.rsa.d) % self.rsa.phi_n, 1)
        self.assertNotEqual(self.rsa.p, self.rsa.q)

if __name__ == '__main__':
    unittest.main()
