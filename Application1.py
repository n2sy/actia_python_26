poids = float(input("Entrez le poids du colis : "))
prix = float(input("Entrez le prix du colis : "))
zone = input("Entrez la zone (A, B ou C): ").upper()
premium = input("Etes-vous premium (Oui / Non): ").upper() == "oui".upper()

if zone == "A":
    livraison = 5
elif zone == "B":
    livraison = 12
else:
    livraison = 25
# elif(zone == "C"):
#     livraison = 25
# else:
#     print("Hors zone")

if poids > 10:
    surcharge = (poids - 10) * 2
    livraison += surcharge

if (premium or prix > 150) and (poids < 30):
    livraison *= 0.5


print(f"Les frais de livraison sont : {livraison + prix} dinars")
