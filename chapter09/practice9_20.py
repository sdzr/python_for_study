import gzip
#compress
f_in=open('test.txt','rb')
f_out=gzip.open('test.txt.gz','wb')
f_out.writelines(f_in)
f_in.close()
f_out.close()

#decompress

f_out=open('test.txt','wb')
f_in=gzip.open('test.txt.gz','rb')
f_out.write(f_in.read())
f_out.close()
f_in.close()



