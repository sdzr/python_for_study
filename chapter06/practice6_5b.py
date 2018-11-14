a=input("input a strs:")
b=input("input a strs:")
trigger=''
if len(a)==len(b):
    trigger=False
else:
    for i in range(len(a)):
        if a[i]!=b[i]:
            trigger=False
            break
        else:
            trigger=True

if trigger:
    print("String A matches string B")
else:
    print("String A not matches string B")

