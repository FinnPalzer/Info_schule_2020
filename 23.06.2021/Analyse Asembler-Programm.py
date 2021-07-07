def fibonaccilulu (eingabe):
    x1 = 1
    x2 = 1
    erbebnis3 = 0
    x5 = 2

    eingabe = eingabe - x5
    
    while(eingabe != 0):
        if (eingabe != 0):
            ergebnis3 = x1 +x2
            x1 = x2
            x2 = ergebnis3
            eingabe = eingabe -1

        else:
            pass
    return ergebnis3