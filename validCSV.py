'''
Created on 01.02.2018

@author: tfuss001
'''

import re

class Syntaxfehler(Exception):
    pass

class Spaltenfehler(Exception):
    pass

def validCSV(filename = None):
    pattern = re.compile(r'^"[0-9]+","[a-zA-Z]+","[a-zA-Z]+"$')
    for line in filename:
        if not line.startswith("#"):
            line = line.strip()
            if pattern.match(line):
                line = line.split(",")
                if len(line) == 3:
                    print(line)
                else:
                    raise Spaltenfehler("falsche Spaltenanzahl")
        else:
            if line.startswith("#"):
                pass
            else:
                raise Syntaxfehler("Syntaxfehler")
    


validCSV(open('./personen.txt',"r"))

