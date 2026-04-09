code_pairs = range(100, 121, 2)
print(code_pairs)
stock_A = list(code_pairs)
print(stock_A)
stock_B = list(range(150, 109, -10))
print(stock_B)
# inventaire_global= []
# inventaire_global.extend(stock_A)
# inventaire_global.extend(stock_B)
inventaire_global = stock_A + stock_B
inventaire_global.extend([200, 201, 202])

print(f"{'110 est bien présent' if(110 in inventaire_global) else '110 est absent'}")
print(
    f"{'999 est bien présent' if(999 not in inventaire_global) else '999 est absent'}"
)


indice = inventaire_global.index(120)
print(f"120 se trouve {inventaire_global.count(120)} fois dans la liste")
print(inventaire_global.pop())
inventaire_global.remove(120)
print(sorted(inventaire_global))
inventaire_global.sort(reverse=True)
print(inventaire_global)
print(f"Nombre d'articles restant : {len(inventaire_global)}")
inventaire_global.clear()
