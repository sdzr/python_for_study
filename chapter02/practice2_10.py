T=True
while T:
    num=int(input('输入1到100之间的数：'))
    if 0<=num<=100:
        print('ok')
        T=False
    else:
        print('error')
