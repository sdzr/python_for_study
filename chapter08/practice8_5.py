from practice8_4 import *

def getfactors(num):
    re=list()
    for val in range(2,num+1):
        if isPrime(val):
            while num%val==0:
                re.append(val)
                num=num/val
        else:
            continue
    return re

if __name__=='__main__':
    s=int(input('输入一个整数：'))
    re=getfactors(s)
    for val in re:
        print(val)



