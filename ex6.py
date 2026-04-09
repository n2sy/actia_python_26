nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]

print([i for i in nombres if i % 2 == 0])
print([i for i in range(-10, 11) if i > 0])
print([i * 2 for i in range(0, 5)])
print([i if (i % 2 == 0) else -i for i in range(0, 10)])


for i in range(3):
    pass
print(i)

s = 1 < 2 < 3
print(s)

a = [1, 2, 3, 4, 5, 6]

print(a.pop())
print(a)
