'''
Created on 02.02.2018

@author: tfuss001
'''

dic = {'a':22,'b':42,'c':34,'d':112,}
print(sorted(dic.items(),key = lambda x : x[1], reverse=False))
