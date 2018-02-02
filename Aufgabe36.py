'''
Created on 22.12.2017

@author: tfuss001
'''

lis=[]

#alle Maenner absteigend nach Wohnort sortiert
print(sorted([splitted for splitted in [line.strip().split(";") for line in open("./a36-bonz.txt","r")] if splitted[0] == "Herr"],key=lambda x: x[3]))


#die Summe aller Gehaelter aller Frauen
print(sum([int(splitted[3]) for splitted in [line.strip().split(";") for line in open("./a36-bonz.txt","r")] if splitted[0] == "Frau"]))

#Wohnort der Person, die unter allen, deren Vorname mit "j" beginnt, am meisten verdient
print(max([splitted for splitted in [line.strip().split(";") for line in open("./a36-bonz.txt","r")] if splitted[2].startswith("J")],key=lambda x: x[3]))


#Eine (inhaltlich natuerlich nicht gerechtfertigte) Liste von gehaltsbezogenen Schmaehungen fuer alle Personen
#mit Gehalt ab 100000 Euro in der Form 'Anrede Nachname bekommt mehr, als er/sie
#verdient!' (Beispiel:  'Herr Meier ist bekommt mehr, als er verdient!' oder 'Frau Schmitz bekommt
#mehr, als sie verdient!')
print([ele[0]+" "+ele[1]+" verdient mehr als {pronoun} verdient".format(pronoun="er" if ele[0]=="Herr" else "sie") for ele in [splitted for splitted in [line.strip().split(";") for line in open("./a36-bonz.txt","r")] if int(splitted[3]) >= 100000]])
