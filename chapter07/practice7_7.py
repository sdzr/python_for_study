def dict_change(in_dic):
    out_dic={}
    for key,val in in_dic.items():
        out_dic[val]=key
    return out_dic

if __name__=='__main__':
    in_dic={'a':1,'b':2,'c':3}
    out=dict_change(in_dic)
    for i in out:
        print(out[i])
