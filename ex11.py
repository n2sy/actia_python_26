zoneA = {"Amine", "Sonia", "Mehdi", "Inès"}
zoneB = {"Mehdi", "Inès", "Yassine", "Sami"}

print(f"Les personnes qui sont allés aux deux zones sont {zoneA & zoneB}")
print(f"Les personnes qui sont allés aux deux zones sont {zoneA.intersection(zoneB)}")

print(f"Toutes les personnes des deux zones sont {zoneA | zoneB}")
print(f"Toutes les personnes des deux zones sont {zoneA.union(zoneB)}")
print(f"Toutes les personnes de la zoneA mais pas de B {zoneA - zoneB}")
print(f"Toutes les personnes de la zoneA mais pas de B {zoneA.difference(zoneB)}")
print(f"Différence symétrique {zoneA ^ zoneB}")
print(f"Différence symétrique {zoneA.symmetric_difference(zoneB)}")

zoneA.add("Hamza")
zoneA.discard("Sonia")

if "Mehdi" in zoneA:
    print("Mehdi est bien présent à la zone A")
else:
    print("Mehdi est absent de la zone A")

fs = frozenset([2, 5, 90])
print(fs)
fs.add("Nidhal")
