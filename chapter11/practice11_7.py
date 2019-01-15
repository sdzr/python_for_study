def togather(list1,list2):
    fun=lambda x,y:(x,y)
    return map(None,list1,list2)

a=[1,2,3]
b=['a','b','c']
s=togather(a,b)
print(s)
