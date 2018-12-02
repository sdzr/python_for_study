import os
name=input('输入文件名：')
f=open(name)
size=os.path.getsize(name)
while f.tell()!=size:
    for val in range(10):
        print(f.readline())
    a=input('输入Y继续：')
    if a!='Y':
        break
