import random
from math import gcd

def load_primes(filename="primes.txt"):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f.readlines() if line.strip()]

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

class RSA:
    def __init__(self, p=None, q=None, primes_file="primes.txt"):
        primes = load_primes(primes_file)
        if not p or not q:
            p, q = random.sample(primes[-100:], 2)  # Берём 2 случайных больших простых
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = self.choose_e(self.phi, primes)
        self.d = modinv(self.e, self.phi)

    def choose_e(self, phi, primes):
        for candidate in primes:
            if 1 < candidate < phi and gcd(candidate, phi) == 1:
                return candidate
        raise Exception("No valid e found.")

    def encrypt(self, plaintext):
        # Преобразуем строку в int (через bytes)
        plaintext_bytes = plaintext.encode('utf-8')
        m = int.from_bytes(plaintext_bytes, byteorder='big')
        if m >= self.n:
            raise ValueError("Message too large for the key size")
        c = pow(m, self.e, self.n)
        return c

    def decrypt(self, ciphertext):
        m = pow(ciphertext, self.d, self.n)
        # Переводим int обратно в байты (и в строку)
        num_bytes = (m.bit_length() + 7) // 8
        plaintext_bytes = m.to_bytes(num_bytes, byteorder='big')
        try:
            return plaintext_bytes.decode('utf-8')
        except:
            return plaintext_bytes

