from random import*

#Aufgabe 1)
#a) 
def zufallszahlen_a(anzahl):
    L = []

    for i in range(0,1000):
        L = L + [randint(1,10000)]
    print(L)

#b)
def zufallszahlen_b(anzahl):
    L = []
    summe = 0

    for i in range(0,1000):
        L = L + [randint(1,10000)]
    print(L)

    for element in L:
        summe = summe + element
        durchschnitt = summe / 1000
    print(L)
    print("Durchschnitt:", durchschnitt)

#Aufgabe2)
#a) x=6
def lotto_a(x):
    L = []

    for x in range(0,x):
        L = L + [randint(0,49)]
    print(L)

#b) sollte stimmen x=6
def lotto_b(x):
    L = []

    for x in range(0,x):
        y = randint(0,49)
        while y in L:
            y = randint(0,49)
        L = L + [y]
    print(L)

#Zusatz:

def lotto_zusatz(x):
    L = []

    for x in range(0,x):
        y = randint(0,49)
        while y in L:
            y = randint(0,49)
        L = L + [y]
    print(L)









