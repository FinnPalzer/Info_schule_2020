'''
Programm zur Bestimmung der Geradengleichung
aus zwei gegebenen Punkten
11 Inf GK 1
07.05.2020
'''

# Eingabe - Eingabe der Koordinaten der beiden Punkte
xa = float(input('Bitte geben Sie den x-Wert von Punkt A ein: '))
ya = float(input('Bitte geben Sie den y-Wert von Punkt A ein: '))
xb = float(input('Bitte geben Sie den x-Wert von Punkt B ein: '))
yb = float(input('Bitte geben Sie den y-Wert von Punkt B ein: '))

# Verarbeitung - Berechnung der Funktionsvorschrift
steigung = (yb-ya) / (xb-xa)
y_achsenabschnitt = ya - steigung*xa

# Ausgabe - Ausgabe der berechneten Funktionsvorschrift
print('Steigung: ',steigung)
print('Y-Achsenabschnitt: ',y_achsenabschnitt)
print('Geradengleichung: y=',steigung,'*x+',y_achsenabschnitt)
