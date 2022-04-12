from cProfile import label
from cgitb import text
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror, showinfo

from mysqlx import Column
# from listdesInscrit import list


class personnage():
    def __init__(self, prenom, no, photo):
        self.prenom = prenom
        self.nom = nom
        self.photo = photo

    def __eq__(self, other):
        return(self.prenom == other.prenom and self.nom == other.nom)


def parcourir():
    global imageName
    imn = askopenfilename(initialdir="/", title="selectionner une image",
                          filetypes=(("file png", "*png"), ("file jpg", "*jpg")))
    if imn:
        imageName = imn
    if imageName:
        texte = imageName.split("/")
        photoEntre.configure(text=".../"+texte[-1])


def appartient(liste, val):
    for i in range(len(liste)):
        if liste[i]. __eq__(val):
            return 1
    return 0


def valider():
    global listePersonne, imageName
    photo = imageName
    if prenomEntre.get() and nomEntre.get() and photo:
        pn = personnage(prenomEntre.get(), nomEntre.get(), photo)
        if appartient(listePersonne, pn):
            showerror(title="Formulaire invalide",
                      message="cet utilisateur existe deja !")
        else:
            listePersonne.append(pn)
            showinfo(title="validation reussie",
                     message="{} a ete bien reussi".format(prenomEntre.get()))

    else:
        showerror(title="Formulaire invalide",
                  message=" Toute les champs doivent etre renseigner")


def reinitialiser():
    global imageName
    prenomEntre.delete(0, END)
    nomEntre.delete(0, END)
    imageName = ''
    photoEntre.configure(text='Aucune image selectionner')

    imageName, listePersonne = '', []


fen = Tk()
fen.geometry("300x320+300+150")
fen.title("Page d'inscription")

contenu = Canvas(fen, bg="#FF7800")

fontLabel = 'arial 13 bold'
fontEntre = 'arial 11 bold'

prenom = Label(contenu, text="Votre pronom:",
               font=fontLabel, fg='white', bg='#FF7800')
nom = Label(contenu, text='Votre nom:',
            font=fontLabel, fg='white', bg='#FF7800')
photo = Label(contenu, text='Votre photo:',
              font=fontLabel, fg='white', bg='#FF7800')
validation = Label(contenu, text='Entrer vos info ici:',
                   font=fontLabel, fg='#FF7800', bg='white')

prenomEntre = Entry(contenu, font=fontEntre)
nomEntre = Entry(contenu, font=fontEntre)
photoEntre = Label(contenu, text='Aucune photo selctionner:',
                   font='arial 8 bold', fg='white', bg='#FF7800')
buttonParcourir = Button(
    contenu, text='Pr', command=parcourir, fg='white', bg='#FF7800')

validation.grid(row=0, column=0, columnspan=2)
prenom.grid(row=1, column=0, sticky=E, padx=5, pady=5)
nom.grid(row=2, column=0, sticky=E, padx=5, pady=5)
photo.grid(row=3, column=0, sticky=E, padx=5, pady=5)

prenomEntre.grid(row=1, column=1, padx=5, pady=5)
nomEntre.grid(row=2, column=1, padx=5, pady=5)
photoEntre.grid(row=3, column=1, sticky=W, padx=5, pady=5)
buttonParcourir.grid(row=3, column=1, sticky=E, padx=5, pady=5)

b1 = Button(fen, text='Valider', command=valider,
            width=10, fg='white', bg='#FF7800')
b2 = Button(fen, text='Reinitialiser', command=reinitialiser,
            width=10, fg='white', bg='#FF7800')
b3 = Button(fen, text='Voir la liste', command='',
            width=10, fg='white', bg='#FF7800')

b1.grid(row=4, column=0, pady=5)
b2.grid(row=5, column=0, pady=5)
b3.grid(row=6, column=0, pady=5)

contenu.grid(row=0, column=0, padx=5, pady=5)

fen.mainloop()
