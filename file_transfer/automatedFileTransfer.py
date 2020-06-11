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


#source of working directory

source = 'C:/Users/Grady Mellin/Desktop/Python_Course/Large_Python_Projs/file_transfer/workingDir/'
files = os.listdir(source)
homeOffice = 'C:/Users/Grady Mellin/Desktop/Python_Course/Large_Python_Projs/file_transfer/Home_Office/'

#find and transfer files

today_date = datetime.datetime.today().strftime('%Y-%m-%d')

def autoTransfer():
    for i in files:
        file_stats = os.stat(source+i)
        lastMod = datetime.datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d')
        if lastMod >= today_date:
            print(i)
            shutil.copy(source+i, homeOffice)
#schedule daily transfer            
def scheduleDaily():
    schedule.every().day.at("23:59:59").do(autoTransfer)

        
if __name__ == "__main__":
    scheduleDaily()
    while True:
        schedule.run_pending()
        time.sleep(86399)

        
