def vigenere_encrypt(plaintext, key):
    
    ciphertext = ''  # Результат шифрования
    key = key.lower()  # Приводим ключ к нижнему регистру для унификации
    key_length = len(key)
    key_indices = [ord(k) - ord('a') for k in key]  # Преобразуем буквы ключа в индексы (0-25)
#ord() — встроенная функция в Python, которая принимает строку, 
# содержащую один символ Unicode, и возвращает целое число, представляющее кодовую точку этого символа. 
    for i, char in enumerate(plaintext):  # Проходим по каждому символу исходного текста
        if char.isalpha():  
            # Определяем смещение: ord('A') для заглавных, ord('a') для строчных
            offset = ord('A') if char.isupper() else ord('a')
            key_index = key_indices[i % key_length]  # Индекс буквы ключа, повторяется циклически
            # Шифруем символ по формуле Виженера, с учетом регистра
            encrypted = chr((ord(char) - offset + key_index) % 26 + offset)
            ciphertext += encrypted
        else:
            ciphertext += char  # Неалфавитные символы добавляются без изменений
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    plaintext = ''  # Результат расшифровки
    key = key.lower()  # Приводим ключ к нижнему регистру для унификации
    key_length = len(key)
    key_indices = [ord(k) - ord('a') for k in key]  # Индексы букв ключа

    for i, char in enumerate(ciphertext):  # Проходим по каждому символу шифртекста
        if char.isalpha():  # Если символ - буква
            offset = ord('A') if char.isupper() else ord('a')
            key_index = key_indices[i % key_length]  # Индекс буквы ключа, повторяется циклически
            # Дешифруем символ по формуле Виженера
            decrypted = chr((ord(char) - offset - key_index + 26) % 26 + offset)
            plaintext += decrypted
        else:
            plaintext += char  # Неалфавитные символы добавляются без изменений
    return plaintext