### a)
#Funktion
def teilbar(zahl):          
    if zahl % 17 == 0:
        teilbar = True
    else:
        teilbar = False
    return teilbar

#Hauptprogramm

x = teilbar(17)
print(x)
y = teilbar(100)
print(y)
print(teilbar(171))


### b) Unterteilung in Funktion und Hauptprogramm