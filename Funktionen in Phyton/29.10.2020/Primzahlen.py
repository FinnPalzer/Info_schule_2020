def primzahl(zahl):
    zaehler = 0
    for x in range(zahl,0,-1):
        if (zahl%x==0):
            zaehler = zaehler + 1
    if (zaehler == 2):
        primzahl = True
    else:
        primzahl = False
    return primzahl

zahl = int(input("Zahl: "))
if (primzahl(zahl) == True):
    print("Die Zahl",zahl," ist eine Primzahl.")
else:
    print("Die Zahl",zahl," ist keine Primzahl.")


