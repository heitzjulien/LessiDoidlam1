from tkinter import *
from tkinter import ttk

# Fonction pour récupérer et afficher les données saisies
def submit_form():
    # Récupérer les valeurs des champs de saisie
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    terms = terms_var.get()

    # Afficher un message de confirmation avec les données saisies
    confirmation_label.config(text=f"Nom: {name}\nEmail: {email}\nÂge: {age}\nConditions acceptées: {terms}")

# Création de la fenêtre principale
root = Tk()
root.title("Formulaire de Demande")

# Créer une Frame pour le formulaire
form_frame = Frame(root, padx=20, pady=20)
form_frame.pack(padx=10, pady=10)

# Label pour le champ "Nom"
name_label = Label(form_frame, text="Nom:")
name_label.grid(row=0, column=0, sticky=W, pady=5)
name_entry = Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

# Label pour le champ "Email"
email_label = Label(form_frame, text="Email:")
email_label.grid(row=1, column=0, sticky=W, pady=5)
email_entry = Entry(form_frame, width=30)
email_entry.grid(row=1, column=1, pady=5)

# Label pour le champ "Âge"
age_label = Label(form_frame, text="Âge:")
age_label.grid(row=2, column=0, sticky=W, pady=5)
age_entry = Entry(form_frame, width=30)
age_entry.grid(row=2, column=1, pady=5)

# Case à cocher pour accepter les termes
terms_var = BooleanVar()
terms_check = Checkbutton(form_frame, text="Accepter les conditions", variable=terms_var)
terms_check.grid(row=3, column=0, columnspan=2, pady=10)

# Bouton de soumission
submit_button = Button(form_frame, text="Soumettre", command=submit_form)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Label pour afficher la confirmation
confirmation_label = Label(form_frame, text="", font=("Arial", 10), fg="green")
confirmation_label.grid(row=5, column=0, columnspan=2, pady=10)

# Lancer l'interface
root.geometry("400x300")
root.mainloop()
