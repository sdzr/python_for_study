import random
a=random.randint(0,9)
A=set()
for i in range(a):
    A.update(str(random.randint(1,10)))

print(A)


b=random.randint(0,9)
B=set()
for i in range(a):
    B.update(str(random.randint(1,10)))
print(B)

print(A|B)
print(A&B)

