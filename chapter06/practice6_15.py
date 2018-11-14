import datetime
def convertDate(allDate):
    year=int(allDate.split('/')[2])
    month=int(allDate.split('/')[1])
    day=int(allDate.split('/')[0])
    return (year,month,day)

if __name__=='__main__':
    import sys
    allDate1=sys.argv[1]
    t1=convertDate(allDate1)
    d1=datetime.date(t1[0],t1[1],t1[2])

    allDate2=sys.argv[2]
    t2=convertDate(allDate2)
    d2=datetime.date(t2[0],t2[1],t2[2])

    print((d2-d1).days)



