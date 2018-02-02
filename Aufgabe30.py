'''
Created on 15.12.2017

@author: tfuss001
'''

def ggTr(a,b):
    if a==b:
        return a
    else:
        if a>b: 
            return ggT(a-b,b)
        else :
            return ggT(b-a,a)


def ggT(x, y):
    while x > 0 and y > 0:
        if x >= y:
            x = x - y
        else:
            y = y - x
    return x+y


f = open("./a30-ggts.dat","r")

lis = []
lis2 = []
i=0



#[ggT(int(line),int(line)+1) for line in f if (line%2)==0]

for line in f:
    if (i%2)==0:
        lis.append(int(line.strip()))
        i+=1
    else:
        lis2.append(int(line.rstrip()))
        i+=1
    
newLis = []
newLis = list(map(lambda x,y: ggT(x,y), lis, lis2))

sum = 0
erg = 0
i = 1
for ele in newLis:
    sum += ele
    i+=1
    
print(sum/i)



#print(list[:3:])
#print(list2[:3:])



print(ggTr(0,30)) 
print(ggTr(20,30))
print(ggTr(2,5))
print(ggTr(8,6))
print(ggTr(7,3))