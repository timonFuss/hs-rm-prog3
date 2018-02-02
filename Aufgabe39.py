'''
Created on 14.01.2018

@author: tfuss001
'''

class Messwerte():
    zeitpunkt = None
    temp = None
    
    def __init__(self, *value):
        if len(value) == 1:
            liste = value[0].split(",")
            self.zeitpunkt = liste[0][1:-1]
            self.temp = float(liste[1])
        else:
            self.zeitpunkt = value[0][1:-1]
            self.temp = float(value[1])
            
    def __repr__(self):
        return "Messwerte(\"'{0}'\", {1})".format(self.zeitpunkt, self.temp)
    
    def __eq__(self, other):
        return self.zeitpunkt == other.zeitpunkt and self.temp == other.temp
    
    def __lt__(self, other):
        return self.zeitpunkt < other.zeitpunkt
    
    def __gt__(self, other):
        return self.zeitpunkt > other.zeitpunkt
    
    def __hash__(self):
        return hash((self.zeitpunkt, self.temp))
    


    
line = [line.strip() for line in open("messwerte.csv")]


import random 

print(sorted([random.choice(line) for _ in range(20)]))

mw = Messwerte(line[0])
mw2 = Messwerte(line[1])

my_set = {mw, mw2}
print(my_set)



