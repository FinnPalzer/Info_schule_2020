text = str(input("Bitte geben Sie den Text ein, der überprüft werden soll:"))
buchstabe_input = str(input("Bitte geben sie den Buchstaben ein nachdem gesucht werden soll:"))
zaehler = 0

for i in text:
    if (i == buchstabe_input.lower() or i == buchstabe_input.upper()):
        zaehler = zaehler + 1
    else:
        pass

print("Es sind",zaehler,"",buchstabe_input," ´s in dem Text.")