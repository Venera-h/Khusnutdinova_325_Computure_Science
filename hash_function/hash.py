def simple_hash(input_bytes: bytes) -> bytes:
    """
    Простая хэш-функция: принимает bytes произвольной длины,
    возвращает bytes длиной 32 (256 бит).
    Не для криптографических целей!
    """
    hash_value = 0xCAFEBABECAFEBABECAFEBABECAFEBABE  # 128 бит стартовое значение
    prime = 0x01000193

    for byte in input_bytes:
        hash_value ^= byte
        hash_value = (hash_value * prime) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF  # 128 бит
        # Ротация влево на 7 бит
        hash_value = ((hash_value << 7) | (hash_value >> (128 - 7))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

    # Дублируем хеш чтобы получить 256 бит (32 байта)
    final_hash = (hash_value.to_bytes(16, 'big') + hash_value.to_bytes(16, 'little'))
    return final_hash

if __name__ == "__main__":
    data = b"Hello world"
    h = simple_hash(data)
    print("Simple hash (hex):", h.hex())
    print("Length:", len(h))
