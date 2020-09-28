###Aufgabe: Eingabe nätürliche Zahl             ###
###         Ausgabe nächst größere Quadratzahl  ###
###                                             ###
###                                             ###
#



gefunden = False
nächst_größere_quadratzahl = 0
#Variablen für Überprüfung:
natürliche_zahl = int(input("Bitte geben Sie eine natürliche Zahl an:"))
x = natürliche_zahl



while gefunden == False:
    
    x = x+1 
    wurzel = int(x**0.5)
    check = x / wurzel

    #Überprüfung auf Quadratzahl:
    if check == wurzel:
        gefunden = True

        #Ausgabe:
        print("Die nächst größere Quadratzahl zur Zahl", natürliche_zahl ," ist", nächst_größere_quadratzahl,".")
    else:
        pass
    


else:
    pass





  
