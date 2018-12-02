def factorial(N):
    if N>=2:
        return N*factorial(N-1)
    else:
        return 1

if __name__=='__main__':
    N=int(input('输入一个整数：'))
    print(factorial(N))
