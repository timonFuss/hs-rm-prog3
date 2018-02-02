'''
Created on 11.01.2018

@author: tfuss001
'''

wird = "irjmnzltacogdeksvbphxqyuwf"
aus = list(map(chr, range(97,123)))
wird = list(wird)


import sys
 
#name = sys.argv[1]

print([[word for word in line.split()] for line in open("./hotzenplotz.txt","r")])