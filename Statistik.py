'''
Created on 02.02.2018

@author: tfuss001
'''

def statistiken(dateiname):
    dic = {}
    bool = True
    with open(dateiname) as file:
        lines = [lines.strip().split(";") for lines in file]
        for line in lines:
            bool = True
            #wenn noch nicht im dic -> einfuegen
            if line[0] not in dic:
                dic[line[0]] = [(line[1],int(line[2]))]
            #ansonsten filtern
            else:
                for value in dic.get(line[0]):
                    #wenn die namen gleich sind
                    if value[0] == line[1]:
                        liste = dic.get(line[0])
                        liste = [(ele[0],ele[1] + int(line[2])) for ele in liste if ele[0] == line[1]]
                        dic[line[0]] = liste
                        bool = False
                if bool is True:
                    liste = dic.get(line[0])
                    new = (line[1],int(line[2]))
                    liste.append(new)
                    dic[line[0]] = liste
    return sorted(dic.items())

if __name__ == "__main__":
    diction = statistiken("bestellungen.txt")
    print(diction)