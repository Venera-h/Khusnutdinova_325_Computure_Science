def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            shifted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    text = input("Введите текст для шифрования: ")
    shift = int(input("Введите сдвиг: "))
    encrypted_text = caesar_cipher(text, shift)
    print("Зашифрованный текст:", encrypted_text)