from Crypto.Random import get_random_bytes

def generate_key():
    key = get_random_bytes(32)
    with open("key.bin", "wb") as f:
        f.write(key)
    return key

def get_key():
    with open("key.bin", "rb") as f:
        key = f.read()
    return key
