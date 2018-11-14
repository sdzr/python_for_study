#/usr/bin/python3
import sys
def runnian(num):
    num=int(num)
    if num%4==0:
        if num%100==0:
            print('%d 是世纪闰年'%num)
        else:
            print('%d 是普通闰年'%num)
    else:
        print('%d 不是闰年')
    return
if __name__=='__main__':
    runnian(sys.argv[1])
