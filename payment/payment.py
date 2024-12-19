from tkinter import *
from tkinter import ttk

root = Tk()
root.title("LessiDoidlam1 - Demande de rançon")

root.geometry("1200x600")

root.config(bg="red")

frm = Frame(root, bg="white", width=1000, height=600)
frm.grid_propagate(False)
frm.grid(row=0, column=0, padx=100, pady=100)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

Label(frm, text="LessiDoidlam1\n", bg="white").grid(column=0, row=0)

Label(frm, text="Vos informations personnelles ont été cryptées.\n", bg="white").grid(column=0, row=1)

Label(frm, text="La plupart de vos documents, photos, vidéos et autres fichiers ne sont plus accessible car ils ont été cryptés.\nPeut-être que vous avez essayer de chercher un moyen de restaurer vos fichiers mais ne perdez pas votre temps.\nPersonne ne peut restaurer vos fichiers sans notre service de décryptage.\n", bg="white").grid(column=0, row=2)

Label(frm, text="Puis-je récupérer mes fichiers ?", bg="white").grid(column=0, row=3)

Label(frm, text="Bien sûr. Nous vous garantissons que nous pouvons restaurer tous vos fichiers de manière sécurisé et simple.\n", bg="white").grid(column=0, row=4)

Label(frm, text="Vous avez 3 jours pour valider le paiment. Passer les jours, le prix sera doublé.\nSi vous ne payez pas au bout de 7 jours, vous ne pourrez plus jamais restaurer vos fichiers.\n", bg="white").grid(column=0, row=5)

Label(frm, text="Veuillez procéder au paiement pour récupérer vos informations.\n", bg="white").grid(column=0, row=6)

ttk.Button(frm, text="Payer", command=root.destroy).grid(column=0, row=7)

ttk.Button(frm, text="Quitter", command=root.destroy).grid(column=0, row=10)

root.mainloop()