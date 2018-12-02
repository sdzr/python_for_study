import sys
import shelve
import os
def outSave(filename,ls):
    s=shelve.open(filename,writeback=True)
    if 'db' in s:
        s['db']+=(' '.join(ls[0:3])+os.linesep+ls[3]+os.linesep)
    else:
        s['db']=(' '.join(ls[0:3])+os.linesep+ls[3]+os.linesep)

    s.close()
def output(filename):
    s=shelve.open(filename)
    print(s['db'])
    s.close()
    
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
    if sys.argv[1]=='print':
        output('data.shl')
    else:
        re=operate(sys.argv[1],sys.argv[2],sys.argv[3])
        ls=sys.argv[1:]
        ls.append(str(re))
        outSave('data.shl',ls)
        print(re)





