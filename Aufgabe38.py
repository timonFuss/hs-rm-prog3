'''
Created on 14.01.2018

@author: tfuss001
'''

import itertools

#print(list(itertools.permutations([1,2,3,4])))



def permutationen(seq):
    if len(seq) <=1:
        yield seq
    else:
        for perm in permutationen(seq[1:]):
            for i in range(len(seq)):
                yield perm[:i] + seq[0:1] + perm[i:]
                
obj = permutationen([1,2,3,4])
print(obj.next(),obj.next())
print([ele for ele in permutationen([1,2,3,4,5])])