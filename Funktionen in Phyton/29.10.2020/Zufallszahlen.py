from random import*

def zufallszahlen(anzahl):
    L = []
    while (len(L) < anzahl):
           L = L + [randint(1,1000)]
    return L

anzahl = int(input('Anzahl: '))
x = zufallszahlen(anzahl)
print(x)
