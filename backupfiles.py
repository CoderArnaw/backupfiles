import os
import shutil
source=input("enter the source folder name")
destination=input('enter the destination folder name')
listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file),destination)