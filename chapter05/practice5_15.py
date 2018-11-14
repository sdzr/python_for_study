import sys
def fun1(a,b):
    while b!=0:
        x=a%b
        a=b
        b=x
    return a
if __name__=='__main__':
    m=int(sys.argv[1])
    n=int(sys.argv[2])
    if m<n:
        m,n=n,m
    gy=fun1(m,n)
    gb=m*n/gy
    print(gy,gb)
