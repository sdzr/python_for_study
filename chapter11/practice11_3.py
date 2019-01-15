import functools
max2=lambda x,y:x if x>y else y
min2=lambda x,y:y if x>y else x
print(max2(4,8))
print(min2(4,8))


def myMax(l):
    return functools.reduce(max2,l)
def myMin(l):
    return functools.reduce(min2,l)
s=[3,4,2,7,1,10]

print(myMax(s))
print(myMin(s))
