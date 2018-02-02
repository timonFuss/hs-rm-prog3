'''
Created on 15.12.2017

@author: tfuss001
'''


def h(a,b,c=1000,*d,**e):
    print(a,b,c,d,e)
    
h(17,21)
h(10,20,30)
#h(1,2,3,4,5,6,c=7)
h(1,2,3,4,5,6,x=7,y=22)