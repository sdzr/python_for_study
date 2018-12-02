from practice8_5 import *
def isFullNum(num):
    ls=getfactors(num)
    ls.insert(0,1)
    if ls[-1]==num:
        ls=ls[:-1]
    if num==sum(ls):
        return 1
    else:
        return 0
if __name__=='__main__':
    num=int(input('输入一个整数：'))
    if isFullNum(int(num))==1:
        print('%d 是完全数'%num)
    else:
        print('%d 不是完全数'%num)
