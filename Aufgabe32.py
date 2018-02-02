'''
Created on 11.01.2018

@author: tfuss001
'''

def einlesen():
    lst = [line.rstrip() for line in open("./a32-fahrzeiten.txt","r")]
    lst = list([ele.split(";") for ele in lst])
    print(lst)
    
    
        
            

def auskunft(linie, start, ziel):
    return 1

einlesen()