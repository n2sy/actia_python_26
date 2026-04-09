clients = {
    101: {"nom": "Yasmine", "points": 50, "statut": "Bronze"},
    102: {"nom": "Aymen", "points": 0, "statut": "Bronze"},
    103: {"nom": "Senda", "points": 120, "statut": "Argent"},
    104: {"nom": "Nader", "points": 10, "statut": "Bronze"},
    105: {"nom": "Dina", "points": 0, "statut": "Bronze"},
}

# Liste de transactions : (ID_Client, Montant_Achat)
achats_du_jour = [(101, 45.50), (103, 120.00), (101, 30.00), (102, 15.00)]

for idc, achat in achats_du_jour:
    nbAdd = int(achat // 10)
    clients[idc]["points"] += nbAdd

print(clients)

for idc in clients:
    st = clients[idc]["points"]
    if st >= 150:
        clients[idc]["statut"] = "Or"
    elif st >= 100:
        clients[idc]["statut"] = "Argent"
    else:
        clients[idc]["statut"] = "Bronze"

idASupprimer = []
for idc in clients:
    if clients[idc]["points"] == 0:
        idASupprimer.append(idc)

print(idASupprimer)
for idc in idASupprimer:
    del clients[idc]

print(clients)
for idc, infos in clients.items():
    print(
        f"ID : {idc} | Nom : {infos["nom"]} | Points : {infos["points"]} | Statut : {infos["statut"]}"
    )

# dict = {"prenom": "nidhal", "prenom": "eya", "actia": "hamdi", "annee": 2026}
# print(list(dict))

# print(dict.get("age", 30))
# print(dict["age"])

# # # dict["prenom"] = "Roua"
# # # del dict["annee"]
# # print(dict)


# # # if "actia" not in dict:
# # #     print("Actia est PAS bien une clé")

# # # print(dict.keys())
# # # print(dict.values())
