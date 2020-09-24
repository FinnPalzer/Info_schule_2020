benutzer = input("Bitte Benutzer eingeben:")

if(benutzer != 'Max'):
    print("Benutzer falsch. Zugriff verweigert")
else:
    print("Bitte Passwort für Benutzer",benutzer,"eingeben:")
    passwort = input()
    if(passwort == 'hallo'):
        print("Zugriff gewährt.")
    else:
        print("Zugriff verweigert")






