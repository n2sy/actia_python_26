import random
import sys


def deviner_nombre():
    chiffre_a_deviner = int(random.random() * 50)
    print(chiffre_a_deviner)
    for _ in range(5):
        nb = int(input("Devinez le nombre : "))
        if nb > chiffre_a_deviner:
            print("Donnez un chiffre plus petit")
        elif nb < chiffre_a_deviner:
            print("Donnez un chiffre plus grand")
        else:
            print(f"Bravo, vous avez trouvé en {_+1} essais")
            sys.exit()


deviner_nombre()
