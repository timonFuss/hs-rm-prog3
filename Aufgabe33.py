'''
Created on 22.12.2017

@author: tfuss001
'''

#i.
print([ele*ele*ele for ele in range(1,11) if ele%2==0])

print(list(filter(lambda x: x%2==0,map(lambda x: x*x*x,range(1,11)))))

#ii.
zahl = 123
print([ele for ele in range(2,zahl) if zahl % ele == 0])

print(list(filter(lambda x: zahl%x  == 0 ,map(lambda x: x,range(2,zahl)))))

#iii.
print([x for x in range(10000, 10100) if all(x % y != 0 for y in range(2, x))])