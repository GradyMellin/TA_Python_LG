#### Python ver: 3.8.3
##
#### Author: Grady Mellin
##
#### Purpose: GUI to make file transfers easy and customizable

from tkinter import *
import tkinter as tk

import transferMain
import transferFunc


def load_gui(self):
    #Text Box
    self.tbFrom = Entry(self.master, text = '')
    self.tbFrom.grid(row=0, column=1,  padx=(15,15), pady=(50,2), sticky=W)
    self.tbTo = Entry(self.master, text = '')
    self.tbTo.grid(row=1, column=1, padx=(15,15), pady=(10,2), sticky=W)
    #Labels
    self.lblFromDir = Label(self.master, text = "From Directory: ",)
    self.lblFromDir.grid(row=0, column=0, padx=(30,0), pady=(50,0),sticky= W)
    self.lblToDir = Label(self.master, text = "To Directory: ",)
    self.lblToDir.grid(row=1, column=0, padx=(30,0), pady=(10,0),sticky= W)
    #Buttons
    self.btnFromDir = Button(self.master, text='Browse...', width= 15, height = 1, command=lambda: transferFunc.fromDir(self))
    self.btnFromDir.grid(row=0, column=2, padx=(15,15), pady=(50,0), sticky=W)
    self.btnToDir = Button(self.master, text='Browse...', width= 15, height = 1, command=lambda: transferFunc.toDir(self))
    self.btnToDir.grid(row=1, column=2, padx=(15,15), pady=(10,0), sticky=W)
    self.btnCheck = Button(self.master, text='Check for files...', width= 15, height = 2, command=lambda: transferFunc.check(self))
    self.btnCheck.grid(row=2, column=2, padx=(15,15), pady=(10,10), sticky=W)
    self.btnClose = Button(self.master, text='Close Program', width= 15, height = 2, command=lambda: transferFunc.ask_quit(self))
    self.btnClose.grid(row=2, column=1, padx=(15,15), pady=(10,10), sticky=E)

if __name__ == "__main__":
    pass
