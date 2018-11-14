#random 模块中的几个函数的用法。
#random，rrandint,uniform,choice,shuffle,sample,randrange
from random import *
ls=list()
N=randint(2,100)
for i in range(N):
    ls.append(uniform(0,2**31-1))

ls.sort()

for val in ls:
    print(val)
