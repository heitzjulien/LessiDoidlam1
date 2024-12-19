from tkinter import *
from datetime import datetime, timedelta
from frames.payment_frame import create_payment_frame
from frames.form_frame import create_form_frame
from functions import update_counter

# Création de la fenêtre principale
def main():
    root = Tk()
    root.title("LessiDoidlam1 - Demande de rançon")
    root.geometry("1200x600")
    root.config(bg="red")

    # Chargement du logo et configuration
    logo = PhotoImage(file="./img/LessiDoidlam1.png")
    root.iconphoto(True, logo)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Configuration des frames
    target_date = datetime.now() + timedelta(days=7)
    paymentFrame = create_payment_frame(root, target_date)
    formFrame = create_form_frame(root, target_date)

    # Affichage initial
    paymentFrame.tkraise()
    root.mainloop()

if __name__ == "__main__":
    main()
