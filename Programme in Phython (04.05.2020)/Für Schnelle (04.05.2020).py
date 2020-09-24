"""
Programm zur Aufstellung einer Geradengleichung
Autor:Linda Ziemerle
Datum:04.05.2020
"""
#Eingabe
px=float(input('Koordinate x von Punkt P:'))
py=float(input('Koordinate y von Punkt P:'))
qx=float(input('Koordinate x von Punkt Q:'))
qy=float(input('Koordinate y von Punkt Q:'))
#Verarbeitung
steigung= (qy-py)/(qx-px)
steigung2= -(qx-px)/(qy-py)
yabschnitt= -(steigung*px)+py
yabschnitt2= -(steigung2*px)+py
#Ausgabe
print('Geradengleichung: y=',steigung,'x +',yabschnitt)
print('Orthogonalengleichung: y=',steigung2,'x +',yabschnitt2)
