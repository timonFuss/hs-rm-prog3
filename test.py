'''
Created on 02.02.2018

@author: tfuss001
'''
from operator import itemgetter
import collections

def statistiken(dateiname):
    lines = []
    dic = {}
    bool = False
    with open(dateiname) as file:
        lines = [line.strip().split(";") for line in file]
        lines.sort(key = lambda x : x[1])
    
    print(lines)
    
    for line in lines:
        bool = False
        if line[0] not in dic:
            dic[line[0]]=[(line[1],int(line[2]))]
        else:
            for value in dic.get(line[0]):
                if line[1] == value[0]:
                    liste = dic.get(line[0])
                    liste = [(ele[0],int(ele[1])+int(line[2])) if ele[0] == line[1] else (ele[0], ele[1]) for ele in liste]
                    dic[line[0]] = liste
                    bool = True
            if not bool:
                liste = dic.get(line[0])
                liste.append((line[1],line[2]))
                dic[line[0]] = liste
                bool = False
    
    dic = collections.OrderedDict(sorted(dic.items()))
                
    for key, liste in dic.items():
        string = key+ ": "
        string2 = ""
        for ele in liste:
            string2 = "".join(string2 + str(ele[0])+"("+str(ele[1])+") ")            
        string = "".join(string + string2)
        print(string)

    
        
    
statistiken("bestellungen.txt")