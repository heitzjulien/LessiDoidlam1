import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

folder = "../dossier_confidentiel"


def decrypt_file(path, key, output_path=None):

    if output_path is None:
        output_path = path.replace('.enc', '')

    with open(path, 'rb') as f:

        iv = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = unpad(cipher.decrypt(ciphertext), AES.block_size)


    with open(output_path, 'wb') as f:
        f.write(data)

    print(f"File {path} successfully decrypted in {output_path}")

def decrypt_folder(folder_path, key):

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.enc'):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)
                os.remove(file_path)
    os.remove("key.bin")