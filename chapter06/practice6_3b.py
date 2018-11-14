s=input("输入数字:")
s=s.split()
s=[int(x) for x in s]
def myCmp(a,b):
    return cmp(a,b)

#s.sort(cmp=myCmp)
print(s)




