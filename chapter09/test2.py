import os
for tmpdir in ('/tmp','c:\temp'):
    if os.path.isdir(tmpdir):
        break
else:
    print('no tmp directory available')
    tmpdir=''

if tmpdir:
    os.chdir(tmpdir)
    cwd=os.getcwd()
    print(cwd)

    os.mkdir('example')
