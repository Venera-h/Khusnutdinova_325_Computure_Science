def create_cipher_table(key):
   
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Убираем повторяющиеся символы из ключа и сохраняем порядок
    key = "".join(sorted(set(key.upper()), key=lambda k: key.index(k)))
    # Добавляем оставшиеся буквы алфавита, которых нет в ключе
    table = key + ''.join([ch for ch in alphabet if ch not in key])
    return table

def encrypt(text, key, shift):

    table = create_cipher_table(key)
    result = []
    for char in text.upper():
        if char in table:
            index = (table.index(char) + shift) % len(table)
            result.append(table[index])
        else:
            result.append(char)  # Оставляем пробелы и другие символы без изменений
    return ''.join(result)

def decrypt(ciphertext, key, shift):
    table = create_cipher_table(key)
    result = []
    for char in ciphertext.upper():
        if char in table:
            index = (table.index(char) - shift) % len(table)
            result.append(table[index])
        else:
            result.append(char)  

if __name__ == "__main__":
    text = "HELLO WORLD"
    key = "SECRET"
    shift = 3
    encrypted = encrypt(text, key, shift)
    decrypted = decrypt(encrypted, key, shift)
    print("Original:", text)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
