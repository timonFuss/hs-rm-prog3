'''
Created on 02.02.2018

@author: tfuss001
'''


def statistiken(dateiname):
    lines = []
    dic = {}
    bool = False
    with open(dateiname) as file:
        lines = [line.strip().split(";") for line in file]
    
    for line in lines:
        bool = False
        if line[0] not in dic:
            dic[line[0]]=[(line[1],int(line[2]))]
        else:
            for value in dic.get(line[0]):
                if line[1] == value[0]:
                    liste = dic.get(line[0])
                    liste = [(ele[0],ele[1]+int(line[2])) for ele in liste if ele[0] == line[1]]
                    dic[line[0]] = liste
                    bool = True
            if not bool:
                liste = dic.get(line[0])
                print(liste)
                liste.append((line[1],line[2]))
                dic[line[0]] = liste
                bool = False
    
    print(dic)
        
    
statistiken("bestellungen.txt")