name=input("输入模型名：")
module=__import__(name)
d=dir(module)
for val in d:
    print('name:',val)
    print('type:',type(getattr(module,val)))
    print('value:',getattr(module,val))
    print()
