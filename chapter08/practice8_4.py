def isPrime(num):
    count=num//2
    while count>1:
        if num%count==0:
            return False
        else:
            count=count-1
    else:
        return True 

if __name__=='__main__':
   num= input("input a int:")
   T=isPrime(int(num))
   print(T)


