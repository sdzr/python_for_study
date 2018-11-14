#string 模块下的一个类，用于z按照自定义的模板输出，string.Template.
#可以自定义定界符（delimiter）和替换格式（idpattern）。然而貌似没有必要这么做。
from string import Template
s='there are ${howmany} ${lang} quotation'
template_text=Template(s)
print(template_text.substitute(howmany=3,lang='python'))
print(template_text.safe_substitute(howmany=4))

