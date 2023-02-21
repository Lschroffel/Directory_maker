import csv
import os
import shutil
import sys

#destination directories needs to be in first column with files from original source directory in second column
def copyfromheretothere(source,dest):
    sourcefile=source
    source=os.path.join(sourcedir,source)
    if not os.path.exists(dest):
        os.mkdir(dest)
    if os.path.exists(source):
        print(f'copyfile: {source} to destination: {os.path.join(dest, sourcefile)}')
        shutil.copyfile(source, os.path.join(dest, sourcefile))
    else:
        print(f'ERROR: file {source} does not exist in directory')
csvpath=input('enter file path for csv: ')  or 'felsen test.csv'
if os.path.exists(csvpath):
    print('file exists-yay')
else:
    print('file does not exist')
    sys.exit(1)
sourcedir=input('enter file path for image source directory: ') or 'images'
if os.path.exists(sourcedir):
    print('source dir exists-yay')
    with open(csvpath) as csvfile:
        reader=csv.reader(csvfile, dialect='excel')
        for row in reader:
            print(row[1])
            copyfromheretothere(row[1],row[0])
