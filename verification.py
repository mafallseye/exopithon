# system de verification de mot de passe
password = input("Entrer votre mot de passe")
password_length = len(password)
# verification si le mot de passe est inferieur à 8 caracteres
if password_length <= 8:
    print("le mot de passe est trop court")
elif password_length > 8 and password_length <= 12:
    print("mot de passe moyen")
else:
    print("mot de passe valide")
    print(password_length)
#exercice: place de cinema
#recolterl'age de la persone"quel est l'age de la personne?
#si l'age est mineur-->7£
#si l'age est majeur-->12£
#Souhaitez vous du pop corn?
#si oui-->+5£
#afficher ce prix total a payer