import os
import sys
path=os.path.abspath('./')
path=os.path.join(path,sys.argv[1])
contents=''
f=open(path)
try:
    for line in f:
        line=line.split()
        if len(line) <= 10:
            contents+=' '.join(line)+os.linesep
        else:
            contents+=' '.join(line[0:10])+os.linesep+' '.join(line[10:])
finally:
    f.close()
f=open('test4','w')
f.writelines(contents)
f.close()
