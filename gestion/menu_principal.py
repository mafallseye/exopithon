# les bibliothéques à importé

import tkinter
import cProfile
from subprocess import call
from tkinter import *
from tkinter import ttk, Tk
from tkinter import messagebox
import mysql.connector as MC


def Ajouter():
    matricule = textnumero.get()
    nom = textnom.get()
    prenom = textprenom.get()
    sexe = valeurSex.get()
    classe = comboclasse.get()
    matiere = textmatiere.get()
    note = textnote.get()


mabase = MC.connect(
    host='localhost', user='root', database='note_eleve', password='admin')
meConnect = mabase.cursor()

try:
    sql = "insert into note (code,nom,prenom,sexe,classe,matiere,notes) values(%s, %s, %s , %s, %s, %s,%s)"
    val = (matricule, nom, prenom,  sexe, classe, matiere, note)
    meConnect.execute(sql, val)
    mabase.commit()

    derniereMaricule = meConnect.lastrowid
    messagebox.showinfo("information", "note ajouter")
    root.destroy()
    call(["python", "python310/pithon/gestion/menu_principal.py"])
except Exception as e:
    print(e)

    # retour
    # mabase.rollback()
    # mabase.close()


def Modifier():
    matricule = textnumero.get()
    nom = textnom.get()
    prenom = textprenom.get()
    sexe = valeurSex.get()
    classe = comboclasse.get()
    matiere = textmatiere.get()
    note = textnote.get()


mabase = MC.connect(
    host='localhost', user='root', database='note_eleve', password='admin')
meConnect = mabase.cursor()

try:
    sql = "update note set nom=%s, prenom=%s, sexe=%s, classe=%s, matiere=%s, notes=%s WHERE code=%s"
    val = (nom, prenom,  sexe, classe, matiere, note, matricule)
    meConnect.execute(sql, val)
    mabase.commit()

    derniereMaricule = meConnect.lastrowid
    messagebox.showinfo("information", "note modifier")
    root.destroy()
    call(["python", "python310/pithon/gestion/menu_principal.py"])
except Exception as e:
    print(e)

    # # retour
    # mabase.rollback()
    # mabase.close()


def Supprimer():
    matricule = textnumero.get()


mabase = MC.connect(
    host='localhost', user='root', database='note_eleve', password='admin')
meConnect = mabase.cursor()

try:
    sql = "DELETE FROM note WHERE code=%s"
    val = (matricule, )
    meConnect.execute(sql, val)
    mabase.commit()

    derniereMaricule = meConnect.lastrowid
    messagebox.showinfo("information", "note supprimer")
    root.destroy()
    call(["python", "python310/pithon/gestion/menu_principal.py"])
except Exception as e:
    print(e)

    # retour
    mabase.rollback()
    mabase.close()


# ma fenetre
root = Tk()
root.title("Menu principal")
root.geometry("1350x700+0+0")
root.resizable(False, False)
root.configure(bg="#091821")

# ajouter le titre
lbltitre = Label(root, borderwidth=3, relief=SUNKEN, text="Gestion notes des etudiants", font=(
    "sans serif", 25), bg="#2F4F4F", fg="#FFFAFA")
lbltitre.place(x=0, y=0, width=1350, height=100)

# matricule
lblnumero = Label(root, text="MATRICULE", font=(
    "Arial", 18), bg="#091821", fg="white")
lblnumero.place(x=70, y=150, width=150)
textnumero = Entry(root, bd=4, font=("arial", 14))
textnumero.place(x=250, y=150, width=200)

# nom
lblnom = Label(root, text="Nom", font=(
    "Arial", 18), bg="#091821", fg="white")
lblnom.place(x=70, y=200, width=150)
textnom = Entry(root, bd=4, font=("arial", 14))
textnom.place(x=250, y=200, width=300)

# prenom
lblprenom = Label(root, text="Prenom", font=(
    "Arial", 18), bg="#091821", fg="white")
lblprenom.place(x=70, y=250, width=150)
textprenom = Entry(root, bd=4, font=("arial", 14))
textprenom.place(x=250, y=250, width=300)

# sexe
valeurSex = StringVar()
lblsexemasculin = Radiobutton(root, text="Masculin", value="M", variable=valeurSex, indicatoron=0, font=(
    "Arial", 14), bg="#091821", fg="#696969")
lblsexemasculin.place(x=250, y=300, width=130)
lblsexefeminin = Radiobutton(root, text="Feminin", value="F", variable=valeurSex, indicatoron=0, font=(
    "Arial", 14), bg="#091821", fg="#696969")
lblsexefeminin.place(x=420, y=300, width=130)

# classe
lblclasse = Label(root, text="Classe", font=(
    "Arial", 18), bg="#091821", fg="white")
lblclasse.place(x=70, y=350, width=150)

comboclasse = ttk.Combobox(root, font=("Arial", 14))
comboclasse["values"] = ['CP', 'CE1', 'CE2',
                         'CM1', 'CM2', '6e', '5e', '4e', '3e']
comboclasse.place(x=250, y=350, width=130)

# matiere
lblmatiere = Label(root, text="MATIERE", font=(
    "Arial", 18), bg="#091821", fg="white")
lblmatiere.place(x=70, y=400, width=150)
textmatiere = Entry(root, bd=4, font=("arial", 14))
textmatiere.place(x=250, y=400, width=300)

# note
lblnote = Label(root, text="Note", font=(
    "Arial", 18), bg="#091821", fg="white")
lblnote.place(x=70, y=450, width=150)
textnote = Entry(root, bd=4, font=("arial", 14))
textnote.place(x=250, y=450, width=200)

# enregistrer
btnEnregistrer = Button(root, text="Enregistrer", font=(
    'arial', 16), bg="#02691E", fg="white", command=Ajouter)
btnEnregistrer.place(x=250, y=500, width=200)

# modifier
btnmodifier = Button(root, text="Modifier", font=(
    'arial', 16), bg="#02691E", fg="white", command=Modifier)
btnmodifier.place(x=250, y=550, width=200)

# Supprimer
btnsupprimer = Button(root, text="Supprimer", font=(
    'arial', 16), bg="#02691E", fg="white", command=Supprimer)
btnsupprimer.place(x=250, y=600, width=200)

# table
table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7),
                     height=5, show="headings")
table.place(x=560, y=150, width=790, height=150)

# entete
table.heading(1, text="MAT")
table.heading(2, text="NOM")
table.heading(3, text="PRENOM")
table.heading(4, text="SEXE")
table.heading(5, text="CLASSE")
table.heading(6, text="MATIERE")
table.heading(7, text="NOTE")

# definir les dimensions des colonnes
table.column(1, width=50)
table.column(2, width=150)
table.column(3, width=150)
table.column(4, width=100)
table.column(5, width=50)
table.column(6, width=100)
table.column(7, width=50)

# afficher les informations de la table
mabase = MC.connect(
    host='localhost', user='root', database='note_eleve', password='admin')
meConnect = mabase.cursor()
meConnect.execute("SELECT * FROM note")

for row in meConnect:
    table.insert('', END, value=row)
    mabase.close()

# execution
root.mainloop()
