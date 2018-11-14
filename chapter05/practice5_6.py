import sys
def operate(N1,op,N2):
    N1=float(N1)
    N2=float(N2)
    s=['+','-','*','/','%','**']
    if op==s[0]:
        return N1+N2
    if op==s[1]:
        return N1-N2
    if op==s[2]:
        return N1*N2
    if op==s[3]:
        return N1/N2
    if op==s[4]:
        return N1%N2
    if op==s[5]:
        return N1**N2
    print(N1,op,N2)
    return 'erorr'

if __name__=='__main__':
   re=operate(sys.argv[1],sys.argv[2],sys.argv[3])
   print(re)
