# class Personne:
#     prenom
#     age
#     +
#     sePresenter()
#     candidater()

# p = personne()


class Personne:
    annee = 2026

    def __init__(self, prenomValue, ageValue):
        self.__prenom = prenomValue
        self.__age = ageValue
        print("Je suis le constructeur")

    @property  # GETTER
    def prenom(self):
        return f"Prenom : {self.__prenom}"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, newAge):
        if newAge > 20 and newAge < 50:
            self.__age = newAge
        else:
            self.__age = 0

    def sePresenter(self):
        print("Je m'appelle " + self.prenom)

    def __str__(self):
        return f"Name : {self.__prenom} and i am {self.__age} years old"


p = Personne("nidhal", 432)
print(p.__str__())
print(p)
# p.age = 30
# print(vars(p))
# # p.prenom = "souhaieb"
# # p._Personne__prenom = "souhaieb"
# # print(vars(p))

# # print(p.__dict__)
# p1 = Personne("hamdi", 87)

# print(Personne.annee)
# p1.annee = 2000
# print(p1.annee)
# print(vars(p1))
# print(p1.__dict__)
# p.sePresenter()
# p1.sePresenter()
# p.prenom = "Eya"
# print(vars(p))
# print(p.prenom)
