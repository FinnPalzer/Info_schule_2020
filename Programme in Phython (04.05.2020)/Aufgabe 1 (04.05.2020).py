'''
Programm zur Berechnung der Fallstrecke
11 Inf GK 1
07.05.2020
'''

# Eingabe - Eingabe der Fallzeit t in Sekunden
zeit = float(input('Geben Sie die Fallzeit in Sekunden an:'))

# Verarbeitung - Berechnung der Fallstrecke
fallstrecke = 0.5*9.81*zeit**2

# Ausgabe - Ausgabe der Fallstrecke
print('Fallstrecke: ',fallstrecke,' in m')
