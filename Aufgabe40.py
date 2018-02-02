'''
Created on 19.01.2018

@author: tfuss001
'''
from Aufgabe39 import Messwerte

class Messreihe:
    def __init__(self, value=None):
        lst = []
        for line in value:
            if line not in lst:
                lst.append(line)

a = Messreihe(open('./messwerte.csv',"r"))




