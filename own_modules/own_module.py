print(__name__)
if __name__ == "__main__":
    print("Execution DANS le module")
    print("I am the own module")
else:
    print("Exécution à partir d'un script externe")


def somme(a, b):
    return a + b
