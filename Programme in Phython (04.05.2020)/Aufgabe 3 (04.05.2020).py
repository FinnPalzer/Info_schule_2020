"""
Programm zur Grundstückspreisberechnung
Autor: Linda Ziemerle
Datum: 04.05.2020
"""
#Eingabe
länge=float(input('Länge des Grundstücks (in m):'))
breite=float(input('Breite des Grundstücks (in m):'))
#Verarbeitung
preisprom2=126
fläche= länge*breite
grundstückspreis= fläche*preisprom2
#Ausgabe
print('Fläche des Grundstücks =',fläche,'Quadratmeter')
print('Grundstückspreis =', grundstückspreis,'Euro')
