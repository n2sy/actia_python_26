t = ("Tunis", 36.8065, 10.1815)
print(f"Latitude : {t[1]}")
# t[0] = "Sfax"

donnees_gps = ("Paris", 48.8566, 2.3522)
# ville, lat, lon = donnees_gps[0], donnees_gps[1], donnees_gps[2]
ville, lat, lon = donnees_gps
print(ville, lat, lon)

itineraire = [("Sousse", 140), ("Sfax", 270), ("Gabès", 400)]
for ville, distance in itineraire:
    print(f"La ville de {ville} est à {distance} Km")
    # print(f"La ville de {element[0]} est à {element[1]} Km")

tab = [15, 82, 5, 44, 91]
tMinMax = (min(tab), max(tab))
print(tMinMax)
# l = [3, 5, 8]
# t = ("nidhal", 14, False, l)
# print(t)
# l.append(100)
# print(t)
# # t1 = tuple(["est", 15, 20])
# # t2 = tuple("nidhal")
# # t3 = "nidhal"
# # print(t3)
# # print(t2)

# # for c in "nidhal":
# #     print(c)

# # print(type(t))
# # print(t[1])
# # t[1] = "Eya"
# # print(t)
