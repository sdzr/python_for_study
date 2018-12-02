import os
path=os.path.abspath('./')+'/tmp'
namelist=[f for f in os.listdir(path) if f.endswith('.py')]
modules={}

for f in namelist:
    module=f[:-3]
    modules.setdefault(module,'')
    fpath=path+os.sep+f
    fobj=open(fpath)
    doc=False
    for line in fobj:
        if line.strip().startswith('"""') and line.strip().endswith('"""') and len(line.strip())>6:
            modules[module]+=line
            continue
        elif (line.strip().startswith('"""') or line.strip().startswith(r'"""')) and len(line.strip())>3 :
            doc=True
            modules[module]+=line
            continue
        elif doc:
            if line.strip()=='"""':
                modules[module]+=line
                doc=False
                continue
            else:
                modules[module]+=line
        else:
            continue
    else:
        fobj.close()
hasdoc=[]
nodoc=[]
for key in modules:
    if modules[key]!='':
        hasdoc.append(key)
    else:
        nodoc.append(key)
print("NO DOC:")
for val in nodoc:
    print(val)

print("HAS DOC")
for key in hasdoc:
    print(key)
    print(modules[key])
    print('\n')
