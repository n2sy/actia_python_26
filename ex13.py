import json

{
prop : 
}

mot = input("Saisissez le mot à rechercher")

stream = open("fichier.txt", "r")
i = 0
for line in stream.readlines():
    line.replace(",", " ").replace(".", " ").replace(":", " ").replace(
        "(", " "
    ).replace(")", " ")
    line = line.split()
    for word in line:
        if mot.upper() == word.upper():
            i = i + 1

print(f"Votre mot apparaît {i} fois")
