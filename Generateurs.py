def multiplierParTrois(n):
    res = []
    for x in range(1, n + 1):
        res.append(x * 3)
    return res


tab = multiplierParTrois(500)
print(tab)


def multiplierParTroisGen(n):
    for x in range(1, n + 1):
        yield (x * 3)


tab = multiplierParTroisGen(500)
print(next(tab))
print(next(tab))
print(next(tab))
print(tab.__next__())

s = "formationpythonactia"
s = iter(s)

l = [4, 66, 2, 11]
l = iter(l)

print(next(l))
