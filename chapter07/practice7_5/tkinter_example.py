import tkinter
from tkinter.constants import *
tk=tkinter.Tk()
frame=tkinter.Frame(tk,relief=RIDGE,borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label=tkinter.Label(frame,text='hello world')
label.pack(fill=X,expand=1)
button=tkinter.Button(frame,text="exit",commend=destory)
button.pack(side=BOTTON)
tk.mainloop()
