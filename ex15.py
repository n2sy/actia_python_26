def generer_filter_seuil(limit, type_filter):
    value = 30

    def filtrer():
        nonlocal value
        value += 10
        if type_filter == "HAUT":
            return value > limit
        elif type_filter == "BAS":
            return value < limit

    return filtrer


fct = generer_filter_seuil(50, "HAUT")
print(fct())
print(fct())
print(fct())
print(fct())
