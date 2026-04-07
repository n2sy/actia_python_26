personnes = [
    "Maxime",
    "Martine",
    "Christopher",
    "Carlos",
    "Michael",
    "Eric",
    "Nidhal",
]

# personnes = personnes + ["Eya", "Maher", "Amen"]
personnes.extend(["Eya", "Maher", "Amen"])
print(personnes)

# for i in range(3):
#     print(f"{i+1} : {personnes[i]}")
for i, element in enumerate(personnes):
    print(f"{i+1} : {element}")
    if i == 2:
        break
personnes.pop(3)
print(personnes)

middle = len(personnes) // 2
groupeA = personnes[:middle]
groupeB = personnes[middle:]
# groupeB = personnes[-middle:]
print(groupeA)
print(groupeB)
print(
    f"{'Le compte est bon' if (len(groupeA) + len(groupeB)) == len(personnes) else 'Le Compte est faux' }"
)
