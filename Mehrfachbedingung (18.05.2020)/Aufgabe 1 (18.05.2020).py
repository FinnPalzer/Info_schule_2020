''' 
Programm was entscheidet ob eine Zahl in 2 Intervallen liegt.
'''

eingabe = int(input("Bitte Zahl eingeben:"))
intervall1 = int(input("Bitte kleinste Intevallgrenze angeben:"))
intervall2 = int(input("Bitte höchste Intevallgrenze angeben:"))

if(eingabe > intervall1 and eingabe < intervall2 ):
    print("Die Zahl",eingabe,"liegt im Intervall[",intervall1,";",intervall2,"].")
else:
    print("Die Zahl",eingabe,"liegt nicht *im Intervall[",intervall1,";",intervall2,"].")