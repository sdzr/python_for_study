import sys
def int2Ip(number):
    re=''
    for i in range(3,-1,-1):
        re=re+str(number//(256**i))+'.'
        if (number//(256**i))>256:
            print('整数超出了范围！')
            sys.exit(1)
        number=number%(256**i)
    return re.rstrip('.')

if __name__=='__main__':
    number=int(sys.argv[1])
    s=int2Ip(number)
    print(s)

