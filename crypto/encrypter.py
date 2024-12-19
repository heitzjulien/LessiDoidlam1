import os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = get_random_bytes(32)
with open("key.bin", "wb") as f:
    # Générer une clé AES de 256 bits
    f.write(key)
folder = "../dossier_confidentiel"


def encrypt_file(path,key,output_path =None):
    try:

        if output_path is None:
            output_path = path + '.enc'

        with open(path, 'rb') as f:
            data = f.read()

        # iv = vecteur d'initialisation
        # En gros, c'est une value aléatoire utiliser pour le chiffrement de même données avec la même clé mais on y sorte des données diff

        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))

        with open(output_path, 'wb') as f:
            f.write(iv + ciphertext)

        print(f"File {path} successfully crypted in {output_path}")

    except Exception as e:
        print(e)

def encrypt_folder(folder_path, key):
    try:
        print(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:

                file_path = os.path.join(root, file)
                encrypt_file(file_path, key)
                os.remove(file_path)

    except Exception as e:
        print(e)
