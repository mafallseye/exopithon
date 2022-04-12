wallet = 5000
price = 1000
# le prix de l'ordinateur est inferieur à 1000
if price <= wallet:
    print("l'achat est possible")
    wallet -= price
else:
    print("l'achat est impossible vous n'avait que {}£".format(wallet))
    ("l'achat est possible", "l'achat est impossible")[price <= 1000]
    print(wallet)
