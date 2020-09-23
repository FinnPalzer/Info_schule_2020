text = str(input("Bitte geben Sie den Text ein, der überprüft werden soll:"))
zaehler = 0

for i in text:
    if (i == 'e'):
        zaehler = zaehler + 1
    else:
        pass

if (zaehler > 5) and (zaehler < 10):
    print("Es sind zwischen 5 und 10 'e' im Text!")
else:
    print("Es sind nicht zwischen 5 und 10 'e' im Text!")
