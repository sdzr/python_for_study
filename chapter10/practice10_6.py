def try_open(filename,mode='r'):
    try:
        f=open(filename,mode)
    except IOError:
        return None
    return f
if __name__=='__main__':
    import sys
    print(try_open(sys.argv[1],sys.argv[2]))
