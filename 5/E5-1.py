#! /usr/bin/env python

import tkinter

top = tkinter.Tk()
label = tkinter.Label(top, text='Hello world!')
label.pack()
quit = tkinter.Button(top, text='quit', command=top.quit)
quit.pack()
tkinter.mainloop()
