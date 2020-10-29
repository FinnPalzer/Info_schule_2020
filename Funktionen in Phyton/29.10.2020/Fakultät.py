def fakultät(zahl):
    fakultät = 1
    for x in range(zahl,0,-1):
        fakultät = fakultät * x
    return fakultät

zahl = int(input("Fakultät von: "))
x = fakultät(zahl)
print(x)