#!/usr/bin/env python3
import datetime

#mksalt函数，生成一个salt
#crypt采用的是DES加密算法，只适用于密码加密，不适合文件加密
#随机生成的salt由两个随机的字符组成，以64*64=4096种方式扰乱DES算法。密码超过8位数，只截取前8位有效。
#数据库直接保存加密h后的字符串。
#如何验证密码。将加密h后得到的字符串当作salt,加密明文密码，h得到的字符串还是该字符串，如下：
#crypt(pwd,salt)==crypt(pwd,crypt(pwd,salt))
from crypt import crypt,mksalt
import pickle
import os


def creatPkl(filename):
    tmp={}
    if os.path.isfile(filename):
        return
    out=open(filename,'wb')
    pickle.dump(tmp,out)
    out.close()

    
def newuser():
    prompt='login desired: '
    while True:
       name=input(prompt)
       if db.get(name) !=None:
           prompt='name taken,try another:'
           continue
       else:
           break
    pwd=input('passwd: ')
    pwd=crypt(pwd,mksalt())
    tm=datetime.datetime.now()
    db[name.lower()]=[pwd,tm]

def olduser():
    name=input('login:  ')
    name=name.lower()
    passwd=input('passwd:  ')
    passwd=crypt(passwd,db.get(name)[0])
    if passwd==db.get(name)[0]:
        tm1=db.get(name)[1]
        tm2=datetime.datetime.now()
        if (tm2-tm1).seconds<=14400:
            print('you already logged in at :<%s>'%tm1)
            db[name]=[passwd,tm2]
        else:
            print('welcome back ',name)

    else:
        print('login incorrect')

def deluser():
    prompt='name of the user to delete:'
    while True:
        name=input(prompt)
        name=name.lower()
        if db.get(name)!=None:
            del(db[name])
            print('user %s deleted'%name)
            break
        else:
            prompt='no the name,try another:'

def showmenu():
    prompt="""
    (N)ew user login
    (E)xiting user login
    (D)elete a user
    (Q)uit
    Enter choice: """
    done=False
    while not done:
        chosen=False
        while not chosen:
            try:
                choice=input(prompt).strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice='q'
            print('\nyour picked [%s]'%choice)
            if choice not in 'neqd':
                print('invalid option, try again ')
            else:
                chosen=True
            if choice=='q':
                done=True
            if choice=='n':
                newuser()
            if choice=='e':
                olduser()
            if choice=='d':
                deluser()

db={}
if __name__=='__main__':    
    filename='data.pkl'
    creatPkl(filename)
    in_put=open(filename,'rb')
    db=pickle.load(in_put)
    showmenu()
    in_put.close()
    out=open(filename,'wb')
    pickle.dump(db,out)
    out.close()

