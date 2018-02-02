'''
Created on 01.02.2018

@author: tfuss001
'''

def werteGenerator():
    x = 0
    while True:
        yield x
        x = x + 1


def generatorMax(werteGenerator, anzahl):
    i = 0
    while i < anzahl:
        yield next(werteGenerator)
        i += 1

def generatorSprung(werteGenerator, sprungliste):
    i = 0
    idx = 0
    yield next(werteGenerator)
    while True:
        if idx > len(sprungliste)-1:
            break
        while(i < sprungliste[idx]):
            next(werteGenerator)
            i += 1
        i = 0
        idx += 1
        yield next(werteGenerator)

def generatorRueckwaerts(werteGenerator, startwert, endwert):
    i = 0
    liste = []
    while i <= startwert:
        liste.append(next(werteGenerator))
        i += 1
    while i > endwert:
        yield liste[i-1]
        i -= 1
        

sprungliste = [3,4,6]

werte = werteGenerator()
werteMax = generatorMax(werte, 10)
werteSprung = generatorSprung(werte, sprungliste)
werteRueck = generatorRueckwaerts(werte, 5, 1)
for ele in werteRueck:
    print(ele)

