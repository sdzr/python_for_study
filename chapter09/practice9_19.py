import random
import sys
def creatFile(value,count,lenth):
    n=lenth-count
    ls=[]
    for i in range(n):
        val=random.randint(0,255)
        if val==value:
            ls.append(chr(val))
        elif val!=value and val==0:
            val=random.randint(1,255)
            ls.append(chr(val))
        elif val!=value and val==255:
            val=random.randint(0,254)
            ls.append(chr(val))
        elif val!=value:
            val=random.randint(0,value-1)
            ls.append(chr(val))
    for i in range(count):
        index=random.randint(0,n)
        ls.insert(index,chr(value))

    f=open('test9_19.txt','w')
    f.write(''.join(ls))
    f.close()
if __name__=="__main__":
    creatFile(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))


        


