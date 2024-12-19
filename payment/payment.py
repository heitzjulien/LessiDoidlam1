from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta

root = Tk()
logo = PhotoImage(file="./img/LessiDoidlam1.png")
root.title("LessiDoidlam1 - Demande de rançon")
root.iconbitmap("./img/LessiDoidlam1.ico")
root.iconphoto(True, logo)
root.geometry("1200x600")
root.config(bg="red")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def update_counter():
    # Recalculer la date actuelle et la date cible (7 jours à partir d'aujourd'hui)
    current_date = datetime.now()
    target_date = current_date + timedelta(days=7)
    
    # Calculer la différence entre la date cible et la date actuelle
    remaining_time = target_date - current_date
    
    # Vérifier si la différence de temps est positive (sinon on arrête le compteur)
    if remaining_time.total_seconds() > 0:
        # Extraire les jours, heures, minutes et secondes de la différence
        remaining_days = remaining_time.days
        remaining_seconds = remaining_time.seconds
        remaining_hours = remaining_seconds // 3600  # Calcul des heures
        remaining_minutes = (remaining_seconds % 3600) // 60  # Calcul des minutes
        remaining_seconds = remaining_seconds % 60  # Reste des secondes

        # Mettre à jour le label avec le temps restant (jours, heures, minutes, secondes)
        counter_label.config(text=f"Il reste {remaining_days} jour(s), "
                                 f"{remaining_hours:02}:{remaining_minutes:02}:{remaining_seconds:02} avant la fin.")
    else:
        # Si le compte à rebours est terminé
        counter_label.config(text="Le délai est terminé.")

    # Mettre à jour le compteur toutes les 1000 ms (1 seconde)
    root.after(1000, update_counter)

def show_payment_frame():
    formFrame.grid_forget()
    paymentFrame.grid(row=0, column=0, padx=100, pady=100)

def show_form_frame():
    paymentFrame.grid_forget()
    formFrame.grid(row=0, column=0, padx=100, pady=100)

def submit_form():
    # Récupérer les valeurs des champs de saisie
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    terms = terms_var.get()

    # Afficher un message de confirmation avec les données saisies
    confirmation_label.config(text=f"Nom: {name}\nEmail: {email}\nÂge: {age}\nConditions acceptées: {terms}")

paymentFrame = Frame(root, bg="white", width=1000, height=600)
paymentFrame.grid_propagate(False)

counter_label = Label(paymentFrame, text="", bg="white")
counter_label.grid(row=10, column=0, pady=20)
update_counter()

Label(paymentFrame, text="LessiDoidlam1\n", bg="white").grid(column=0, row=0)
Label(paymentFrame, text="Vos informations personnelles ont été cryptées.\n", bg="white").grid(column=0, row=1)
Label(paymentFrame, text="La plupart de vos documents, photos, vidéos et autres fichiers ne sont plus accessible car ils ont été cryptés.\nPeut-être que vous avez essayer de chercher un moyen de restaurer vos fichiers mais ne perdez pas votre temps.\nPersonne ne peut restaurer vos fichiers sans notre service de décryptage.\n", bg="white").grid(column=0, row=2)
Label(paymentFrame, text="Puis-je récupérer mes fichiers ?", bg="white").grid(column=0, row=3)
Label(paymentFrame, text="Bien sûr. Nous vous garantissons que nous pouvons restaurer tous vos fichiers de manière sécurisé et simple.\n", bg="white").grid(column=0, row=4)
Label(paymentFrame, text="Vous avez 3 jours pour valider le paiment. Passer les jours, le prix sera doublé.\nSi vous ne payez pas au bout de 7 jours, vous ne pourrez plus jamais restaurer vos fichiers.\n", bg="white").grid(column=0, row=5)
Label(paymentFrame, text="Veuillez procéder au paiement pour récupérer vos informations.\n", bg="white").grid(column=0, row=6)
ttk.Button(paymentFrame, text="Payer", command=show_form_frame).grid(column=0, row=7)
# ttk.Button(paymentFrame, text="Quitter", command=root.destroy).grid(column=0, row=10)


formFrame = Frame(root, bg="white", width=1000, height=600)
formFrame.grid_propagate(False)
# formFrame.grid(row=0, column=0, padx=100, pady=100)
Label(formFrame, text="LessiDoidlam1\n", bg="white").grid(column=0, row=0)
Label(formFrame, text="Remplir le formulaire\n", bg="white").grid(column=0, row=1)

name_label = Label(formFrame, text="Nom:", bg="white")
name_label.grid(row=2, column=0, sticky=W, pady=5)
name_entry = Entry(formFrame, width=30)
name_entry.grid(row=2, column=1, pady=5)


email_label = Label(formFrame, text="Email:", bg="white")
email_label.grid(row=3, column=0, sticky=W, pady=5)
email_entry = Entry(formFrame, width=30)
email_entry.grid(row=3, column=1, pady=5)


age_label = Label(formFrame, text="Âge:", bg="white")
age_label.grid(row=4, column=0, sticky=W, pady=5)
age_entry = Entry(formFrame, width=30)
age_entry.grid(row=4, column=1, pady=5)


terms_var = BooleanVar()
terms_check = Checkbutton(formFrame, text="Accepter les conditions", bg="white", variable=terms_var)
terms_check.grid(row=5, column=0, columnspan=2, pady=10)


submit_button = ttk.Button(formFrame, text="Soumettre", command=submit_form)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)


confirmation_label = Label(formFrame, text="", font=("Arial", 10), fg="green", bg="white")
confirmation_label.grid(row=7, column=0, columnspan=2, pady=10)

ttk.Button(formFrame, text="Retour", command=show_payment_frame).grid(column=0, row=8)


paymentFrame.grid(row=0, column=0, padx=100, pady=100)

root.mainloop()