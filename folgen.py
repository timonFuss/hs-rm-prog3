'''
Created on 01.02.2018

@author: tfuss001
'''

def lucasfolge():
    vorher = 1
    zweiVorher = 2
    yield zweiVorher
    yield vorher
    
    aktuell = vorher + zweiVorher
    
    while True:
        yield aktuell
        aktuell, vorher, zweiVorher = aktuell+vorher, aktuell, vorher
        
        
def pellfolge ():
    vorher = 1 
    zweiVorher = 0
    yield zweiVorher
    yield vorher
    
    aktuell = 2*vorher + zweiVorher
    
    while True:
        yield aktuell
        vorher, zweiVorher = aktuell, vorher
        aktuell = 2*vorher + zweiVorher

pell = pellfolge()
for i in range(10):
    print(next(pell))


folge = lucasfolge()
for i in range(10):
    print(next(folge))


    