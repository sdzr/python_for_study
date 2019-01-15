from random import randint
def leapyear(year):
    if year<1900 or year>2018:
        print('year error')
    elif (year%4==0 and year%100==0) or (year%400==0):
        return year
years=[randint(1900,2018) for i in range(100)]

for val in filter(leapyear,years):
    print(val)


for val in [n for n in [randint(1900,2018)for i in range(100)] if (n%4==0 and n%100==0) or (n%400==0)]:
    print(val)
