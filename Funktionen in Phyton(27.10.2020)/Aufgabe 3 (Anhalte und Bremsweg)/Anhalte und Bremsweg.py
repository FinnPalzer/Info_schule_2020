def reaktionsweg_berechnen(geschwindigkeit):
    reaktionsweg = (geschwindigkeit/10)*3
    return reaktionsweg

def bremsweg_berechnen(geschwindigkeit):
    bremsweg = ((geschwindigkeit(10)*(geschwindigkeit/10)/2))
    return bremsweg

def anhalteweg_berechnen(geschwindigkeit):
    anhalteweg = reaktionsweg + bremsweg
    return anhalteweg

   