releves = [22.5, 25.0, 28.1, 35.0, 42.6, 18.0, 55.0, 40.2]

for element in releves:
    print(int(element))

for element in range(100, 9, -10):
    print(element, "Degrés testés")

pression = 0
while pression < 50:
    pression += 8
    print("La pression a atteint", pression)

for temperature in releves:
    if temperature < 20:
        continue
    elif temperature > 50:
        print("Alerte Critique")
        break
    else:
        print(f"Temperature conforme [{temperature}]")

for i in range(len(releves)):
    releves[i] = f"{(releves[i] * 1.1):.2f}"


print(releves)
