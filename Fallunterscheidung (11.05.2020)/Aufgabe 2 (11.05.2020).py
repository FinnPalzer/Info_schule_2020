zahl1 = int(input("Bitte Zahl 1 eingeben:"))
zahl2 = int(input("Bitte Zahl 2 eingeben:"))

if(zahl1 > zahl2):
    print("Die Zahl",zahl1," ist größer als die Zahl",zahl2,".")
else:
    
    if(zahl1 < zahl2):
        print("Die Zahl",zahl1,"ist kleiner als die Zahl",zahl2,".")
    else:

        if(zahl1 == zahl2):
            print("Die Zahlen sind gleich groß.")