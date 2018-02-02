'''
Created on 25.01.2018

@author: tfuss001
'''
import re


#Datum in der Form TT.MM.JJJJ, (Tag.Monat.Jahr)

pattern = re.compile(r'[\d]{2}.[\d]{2}.[\d]{4}')
match = pattern.match("25.01.2018")
print(match.group())

#Euro-Betraege
pattern = re.compile(r'([\d]{0,3}.)*,[\d]{2}( EUR)?')
match = pattern.match("1.223,56 EUR")
print(match.group())

#Telefonnummern mit optinaler Laenderkennung
pattern = re.compile(r'(\+[\d]{2})?([\/\-]?[\d]{2,*})*')
match = pattern.match("+49-123-123-123")
print(match.group())