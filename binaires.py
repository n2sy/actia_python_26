data = bytearray(100)
data[2] = 100

# with open("text.bin", "wb") as f:
#     f.write(data)

with open("text.bin", "rb") as f:
    f.read()
    contenu = bytearray(f.read())
    f.readinto(contenu)
    print(contenu)
