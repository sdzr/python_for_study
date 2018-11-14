def fun():
    prompt='输入三个整数（以空格隔开）：'
    a=input(prompt)
    f,t,i=[int(m) for m in a.split()]
    for s in range(f,t+1,i):
        print(s)

if __name__=='__main__':
    fun()
    

