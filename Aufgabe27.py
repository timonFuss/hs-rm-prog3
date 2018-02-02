'''
Created on 11.01.2018

@author: tfuss001
'''



def dreh(lst):
    
    if len(lst) == 1:
        return lst
    else:
        print(str(lst[1:]) + "+" + str(lst[0]))
        return dreh(lst[1:]) +[lst[0]]
    

lst=[1,2,3,4,5]
print(dreh(lst))
    
