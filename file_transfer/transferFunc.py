#### Python ver: 3.8.3
##
#### Author: Grady Mellin
##
#### Purpose: Transfer copy of newly created files from working directory to the home office daily

import shutil
import os
import datetime
import schedule
import time
from tkinter import *
import tkinter as tk
from tkinter import filedialog

import transferGUI
import transferMain

#######Basic functions for GUI

def center_window(self, w, h):
    #gets user's screen height and width
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    #calculates x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application"):
        #closes app
        self.master.destroy()
        os.exit(0)
        
def fromDir(self):
    from_directory = (filedialog.askdirectory()+'/')
    self.tbFrom.insert(0,from_directory)
        
def toDir(self):
    to_directory = (filedialog.askdirectory()+'/')
    self.tbTo.insert(0,to_directory)

def check(self):
    srcFrom = self.tbFrom.get()
    srcTo = self.tbTo.get()
    autoTransfer(srcFrom,srcTo)

#source of working directory

#find and transfer files

today_date = datetime.datetime.today().strftime('%Y-%m-%d')

def autoTransfer(srcFrom,srcTo):
    files = os.listdir(str(srcFrom))
    for i in files:
        file_stats = os.stat(srcFrom+i)
        lastMod = datetime.datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d')
        if lastMod >= today_date:
            print("a copy of the file({}) was transferred ".format(i))
            shutil.copy(srcFrom+i, srcTo)
            
#schedule daily transfer            
def scheduleDaily():
    schedule.every().day.at("23:59:59").do(autoTransfer)

def startAutoTransfer():
    scheduleDaily()
    while True:
        schedule.run_pending()
        time.sleep(86399)
    
        
if __name__ == "__main__":
    pass
        
