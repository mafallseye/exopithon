
from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk



def listeInscrit(fenetre, liste):
	newFen = Toplevel(fenetre)
	newFen.geometry("300x400+350+150")
	newFen.title("Listes des inscrits")

	listCan = Canvas(newFen, bg="#FF7800")
	fontLabel = 'arial 11 bold'

	resultat = Label(listCan, text=" liste des inscrits:",
					 font=fontLabel, fg='#FF7800', bg='white')
	prenom = Label(listCan, text=" pronom:",
				   font=fontLabel, fg='white', bg='#FF7800')
	nom = Label(listCan, text="nom:",
				font=fontLabel, fg='white', bg='#FF7800')
	photo = Label(listCan, text="Votre pronom:",
				  font=fontLabel, fg='white', bg='#FF7800')
	status = Label(listCan, text="Aucun inscrit pour le moment:",
				   font='arial 8 bold', fg='white', bg='#FF7800')

	listCan.grid(row=0, column=0)
	resultat.grid(row=0, column=0, columnspan=3)
	photo.grid(row=1, column=0, padx=5, pady=5)
	prenom.grid(row=1, column=1, padx=5, pady=5)
	nom.grid(row=2, column=2, padx=5, pady=5)
	status.grid(row=2, column=0, columnspan=3)

	if liste:
		r = 2
		for p in liste:
			photoLab = Label(listCan, height=50)
			img = Image.open(p.photo)
			img = img.resize((80, 80), Image.ANTIALIAS)
			photoLab.img = ImageTk.PhotoImage(img)
			photoLab.configure(image=photoLab.img)

			pre = Label(listCan, text=p.pronom,
						font=fontLabel, fg='white', bg='#FF7800')
			no = Label(listCan, text=p.nom,
					   font=fontLabel, fg='white', bg='#FF7800')

			photoLab.grid(row=r, column=1)
			pre.grid(row=r, column=2)
			no.grid(row=r, column=3)
			listCan.create_line(9, 55, 355, 55, width=1, fill='white')

			r += 1

			status.configure(
				text="{}inscrit pour le moment ".format(len(liste)))
			status.grid(row=r, column=0, columnspan=3, pady=2)

	newFen.mainloop()
