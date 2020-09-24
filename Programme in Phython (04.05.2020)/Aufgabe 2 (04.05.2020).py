'''
Programm zur Berechnung des Umfangs, der Fläche und
des Durchmessers eines Kreises
11 Inf GK 1
07.05.2020
'''

# Eingabe - Eingabe des Radius
radius = float(input('Geben Sie den Radius in cm an: '))

# Verarbeitung - Berechung von Durchmesser, Umfang und Fläche
durchmesser = 2*radius
umfang = 2*3.14159265*radius
flaeche = 3.14159265*radius**2

# Ausgabe - Ausgabe von Durchmesser, Umfang und Fläche
print('Durchmesser: ',durchmesser,' in cm')
print('Umfang: ',umfang,' in cm')
print('Fläche: ',flaeche,' in cm²')
