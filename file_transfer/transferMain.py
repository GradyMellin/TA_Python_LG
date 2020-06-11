#### Python ver: 3.8.3
##
#### Author: Grady Mellin
##
#### Purpose: Main file for transfering files assignment

from tkinter import *
import tkinter as tk
from tkinter import messagebox

import transferGUI
import transferFunc


#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master = master
        #self.master.minsize(500,300)
        #self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        transferFunc.center_window(self,500,300)
        self.master.title("File Transfer ")
        self.master.configure(bg="#F0F0F0")
        # this protocal method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on the Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: transferFunc.ask_quit(self))
        arg = self.master

        # load in the gui widgets from a separate module,
        # keeping your code comparmentalized and clutter free
        transferGUI.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    transferFunc.startAutoTransfer()
