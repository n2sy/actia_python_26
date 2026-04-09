def affichage(*b):
    print(type(b))
    for argument in b:
        print(argument)


affichage(4, 5, "nidhal")
print("*************")
affichage(6, 12, True, "ACTIA", "Hamdi", 4, 5, "nidhal")
