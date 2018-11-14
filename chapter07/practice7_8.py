#将一个字典按值排序
dic={1:'d',2:'c',3:'b',4:'a'}
d=sorted(dic.items(),key=lambda item:item[1])
for key,val in d:
    print(key,val)

d=dict(d)

for key,val in d.items():
    print(key,val)
