from subprocess import call
from tkinter import Tk, ttk
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor


def Seconnecter():

    surnom = textnomutilisateur.get()
    mdp = textmdp.get()
    if (surnom == "" and mdp == ""):
        messagebox.showerror("", "il faut rentrer les données")
        textmdp.delete("0", "end")
        textnomutilisateur.delete("0", "end")
    elif(surnom == "admin" and mdp == "admin"):
        messagebox.showinfo("", "Bienvenu")
        textmdp.delete("0", "end")
        textnomutilisateur.delete("0", "end")
        root.destroy()
        call(["python", "python310/pithon/gestion/menu_principal.py"])
    else:
        messagebox.showwarning("", "Erreur de connexion")
        textmdp.delete("0", "end")
        textnomutilisateur.delete("0", "end")


# ma fenetre
root = Tk()
root.title("Fenetre de connexion")
root.geometry("400x300+450+200")
root.resizable(False, False)
root.configure(bg="#091821")


# ajouter le titre
lbltitre = Label(root, borderwidth=3, relief=SUNKEN, text="Formulaire de connexion", font=(
    "sans serif", 25), bg="#091821", fg="white")
lbltitre.place(x=0, y=0, width=400)
lblnomutilisateur = Label(root, text="Nom Utilisateur:", font=(
    "Arial", 14), bg="#091821", fg="white")
lblnomutilisateur.place(x=5, y=100, width=150)
textnomutilisateur = Entry(root, bd=4, font=("arial", 13))
textnomutilisateur.place(x=150, y=100, width=200, height=30)

lblmdp = Label(root, text="Mot de passe", font=(
    "Arial", 14), bg="#091821", fg="white")
lblmdp.place(x=5, y=150, width=150)
textmdp = Entry(root, show="*", bd=4, font=("arial", 13))
textmdp.place(x=150, y=150, width=200, height=30)

# bouton de connexion
btnEnregistrer = Button(root, text="Connexion", font=(
    'arial', 16), bg="#FF4500", fg="white", command=Seconnecter)
btnEnregistrer.place(x=150, y=200, width=200)

# execution
root.mainloop()
