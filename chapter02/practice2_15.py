a=list()
for i in range(3):
    a.append(int(input('input:')))
if a[0]>a[1]:
    a[0]=a[0]^a[1]
    a[1]=a[1]^a[0]
    a[0]=a[1]^a[0]

print(a)
