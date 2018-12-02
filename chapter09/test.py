import os
import sys
sys.path.append('./')
f=open('test')
f.tell()
f.seek(0,0)
for val in f.readlines():
    print(val)
    #f.tell()
print(f.tell())
f.seek(0,0)
print(f.tell())
f.seek(10,0)
print(f.tell())
