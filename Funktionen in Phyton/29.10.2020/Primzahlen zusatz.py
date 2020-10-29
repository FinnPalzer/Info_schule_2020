from random import*

def zufallszahlen(anzahl):
    L = []
    while (len(L) < anzahl):
           L = L + [randint(1,1000)]
    return L


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






