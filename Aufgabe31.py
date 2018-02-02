#!/usr/bin/env python
'''
Created on 11.01.2018

@author: tfuss001
'''

import sys

name = sys.argv[1]

#Textzeilen ermittlen
zeilen = 0
woerter = 0
buchstabe = 0
for line in open("./"+name,"r"):
    zeilen += 1
    
    #Woerter ermitteln
    for word in line.split(" "):
        woerter += 1
        
        #Buchstaben zaehlen
        for letter in word:
            if letter != '\n':
                buchstabe+=1
print(zeilen)
print(woerter)
print(buchstabe)

def count_words():
    dic = {}
    ausgabeDic = {}
    for line in open("./"+name,"r"):
        for word in line.split():
            word = word.lower()
            if word in dic.keys():
                dic[word] = dic.get(word) +1
            else:
                dic[word] = 1
                
    #Sortieren des Dicts und Filtern der Key/Value-Paare
    ausgabeDic = {k:v for k,v in dic.items() if v == max(dic.values())}
    lis = list([(k,v) for k,v in dic.items()])
    
    print(sorted(lis, key=lambda tup : (-tup[1],tup[0]))[:25])
            
    return ausgabeDic

def count_chars():
    dic = {}
    ausgabeDic = {}
    for line in open("./"+name,"r"):
        for word in line.split():
            for letter in word:
                letter = letter.lower()
                if letter != '\n':
                    if letter in dic.keys():
                        dic[letter] = dic.get(letter) +1
                    else:
                        dic[letter] = 1
                
    #Sortieren des Dicts und Filtern der Key/Value-Paare
    ausgabeDic = {k:v for k,v in dic.items() if v == max(dic.values())}
    
    lis = list([(k,v) for k,v in dic.items()])
    
    print(sorted(lis, key=lambda tup : (-tup[1],tup[0]))[:25])
            
    return ausgabeDic


print(count_words())
print(count_chars())