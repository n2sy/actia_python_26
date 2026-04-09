# a = 10


# def addition():
#     global b
#     b = 5
#     print(a + b)


# def produit():
# #
#     print(a * b)


# addition()
# produit()

# fct = lambda a, b: a * b

# print(fct(3, 5))


def supA10(n):
    if n >= 10:
        return True
    return False


lst = [5, 12, 34, 10, 4]

print(list(filter(supA10, lst)))
print(list(map(lambda n: n * 2, lst)))
