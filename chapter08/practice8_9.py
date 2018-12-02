def fibanaci(num):
    a,b=1,1
    while num-2:
        a=a+b
        a,b=b,a
        num=num-1
    return b
if __name__=='__main__':
    num=int(input('输入一个整数；'))
    print(fibanaci(num))

