#### Python ver: 3.8.3
##
#### Author: Grady Mellin
##
#### Purpose: Transfer files from one directory to another

import shutil
import os

#set source of file(folder A)
source = 'C:/Users/Grady Mellin/Desktop/Python_Course/Large_Python_Projs/file_transfer/Folder_B/'

#set destination path(folder B)
destination = 'C:/Users/Grady Mellin/Desktop/Python_Course/Large_Python_Projs/file_transfer/Folder_A/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
    
