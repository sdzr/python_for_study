import sys
def fun1(num):
    num=int(float(num)*100)
    cent=[25,10,5,1]
    index=0
    re=list()
    while num:
        re.append(num//cent[index])
        num=num%cent[index]
        index+=1
    if re[0]!=0:
        print('%d 个25美分'%re[0]+'\n')
    if re[1]!=0:
        print('%d 个10美分'%re[1]+'\n')
    if re[2]!=0:
        print('%d 个5美分'%re[2]+'\n')
    if re[3]!=0:
        print('%d 个1美分'%re[3])
    return
if __name__=='__main__':
    fun1(sys.argv[1])
