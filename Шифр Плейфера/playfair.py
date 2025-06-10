import string

class PlayfairCipher:
    def __init__(self, key: str):
        self.size = 5
        self.key_square = self.generate_key_square(key)

    def generate_key_square(self, key: str):
        key = key.upper().replace('J', 'I')
        seen = set()
        alphabet = string.ascii_uppercase.replace('J', '')
        key_string = ''
        for char in key + alphabet:
            if char in alphabet and char not in seen:
                seen.add(char)
                key_string += char
        return [list(key_string[i:i+self.size]) for i in range(0, self.size*self.size, self.size)]

    def find_position(self, char):
        for i, row in enumerate(self.key_square):
            for j, c in enumerate(row):
                if c == char:
                    return i, j
        raise ValueError(f"Character {char} not found in key square")

    def process_text(self, text, encrypt=True):
        text = text.upper().replace('J', 'I')
        result = ''
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i+1] if i+1 < len(text) else 'X'
            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2
            result += a + b
        return result

    def encode_pair(self, a, b):
        ax, ay = self.find_position(a)
        bx, by = self.find_position(b)
        if ax == bx:
            return (self.key_square[ax][(ay+1)%5], self.key_square[bx][(by+1)%5])
        elif ay == by:
            return (self.key_square[(ax+1)%5][ay], self.key_square[(bx+1)%5][by])
        else:
            return (self.key_square[ax][by], self.key_square[bx][ay])

    def decode_pair(self, a, b):
        ax, ay = self.find_position(a)
        bx, by = self.find_position(b)
        if ax == bx:
            return (self.key_square[ax][(ay-1)%5], self.key_square[bx][(by-1)%5])
        elif ay == by:
            return (self.key_square[(ax-1)%5][ay], self.key_square[(bx-1)%5][by])
        else:
            return (self.key_square[ax][by], self.key_square[bx][ay])

    def encrypt(self, plaintext: str):
        text = ''.join([c for c in plaintext.upper() if c in string.ascii_uppercase])
        text = self.process_text(text)
        ciphertext = ''
        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]
            c1, c2 = self.encode_pair(a, b)
            ciphertext += c1 + c2
        return ciphertext

    def decrypt(self, ciphertext: str):
        text = ''.join([c for c in ciphertext.upper() if c in string.ascii_uppercase])
        plaintext = ''
        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]
            c1, c2 = self.decode_pair(a, b)
            plaintext += c1 + c2
        return plaintext
