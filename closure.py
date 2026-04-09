def fctA(a):
    n = a

    def fctB():
        print("n = ", n)
        return n

    return fctB


res = fctA(5)
print(res())
print(res())
res2 = fctA(5)
print(res2())
print(res())
