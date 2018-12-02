import os
def countByte(filename,num):
    path=os.path.abspath('./')
    path=os.path.join(path,filename)
    f=open(path)
    s=f.readlines()
    f.close()
    return s.count(chr(int(num)))

if __name__=="__main__":
    import sys
    print(countByte(sys.argv[1],sys.argv[2]))
