from random import randint
print('Teste deine Kofprechenfähigkeiten')
maximum = 20
genug = False
richtig = True
zähler = 0

while richtig and (not genug):
    print("Noch ein Test?")
    antwort = input("Antwort (j/n):")
    
    if antwort == 'j':
        zahl1 = randint(1,maximum)
        zahl2 = randint(1,maximum)
        produkt = zahl1 * zahl2
        print (zahl1, "*", zahl2)
        ergebniss = int(input("Ergebniss:"))
        
        if ergebniss == produkt:
            zähler = zähler +1
            print("richtig")
            print("Richtige Antworten:",zähler)     ### * Auch unten hin möglich gewesen wenn man das Ergebniss erst am Ende haben will###
        else:
            print ("falsch")
            print ("richtig gewesen wäre",produkt)
            richtig = False
    else:
        genug = True
        ### * ###