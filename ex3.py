# prenom = "nidhal"
# nom = "jelassi"

# s = "Je m'appelle {} -- {}".format(prenom, nom)
# print(s)
prix_HT = input("Donnez le prix : ")
montant = input("Entrez le montant dont vous disposez : ")

prix_TTC = int(prix_HT) * 1.19
print(prix_TTC)

if float(montant) < prix_TTC:
    print(
        f"Vous ne pouvez pas vous l'offrir, il vous manque {(prix_TTC - int(montant)):.2f} dinars"
    )
else:
    print(
        f"Vous pouvez vous l'offrir, il vous reste {(int(montant) - prix_TTC):.2f} dinars"
    )
