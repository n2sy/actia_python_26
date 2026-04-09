s = """nidhal en
python"""
print(ord("a"))
print(chr(97))
print(len(s))

s1 = "actia"
s2 = " es "
print((s1 + s2) * 3)
print(s1.index("tia"))
print(s1.find("t", 4))
print(s1.rfind("t", 2, 5))

s3 = "abc"
s4 = "1234a"
print(s3.isalpha())
print(s3.isalnum())
print(s4.isdigit())
s5 = "\t"
print(s5.isspace())

s6 = "-abc-"
print(s6.isupper())
print(s6.islower())

print(s6.join(["xxx", "ccc", "vvv"]))

s7 = "formation python:actia -- python"
print(s7.split(":"))

s7 = s7.replace("python", "ruby")
print(s7)

print(sorted("txpnez"))

print(ord("e"))
print(ord("z"))
if "e" < "z":
    print("Supérieur")
else:
    print("Inférieur")

print(sorted(["tgv", "ert", "zsw"]))
print("******************")
s9 = "txpnez"
print(sorted(s9))
print(s9)
l = ["wsx", "bgggg", "abc"]
sorted(l)
print(l)

print(float("4.15"))

print("abc".rfind("z"))
