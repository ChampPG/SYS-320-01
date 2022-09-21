# File to traverse a given directory and it's subdirs and retrieve all the files.
import os, sys
from sys import platform

# Get information from the command line
#print(sys.argv)

# Direcotry to traverse
rootdir = sys.argv[1]

# print(rootdir)

# In our story, we will traverse a direcotry

# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print('invalid dir => {}'.format(rootdir))
    exit()

# List to save files
fList = []

# Crawl through the provided directory
for root, subfolders, filenames in os.walk(rootdir):
    
    for f in filenames:
        # print(root + '\\' + f)

        # If linux system
        if platform == 'linux' or platform == 'linux2':
            fileList = root + '/' + f

        # If OS X System
        # elif platform == 'darwin':

        # If windows system
        elif platform == 'win32':   
            fileList = root + '\\' + f

        #print(fileList)
        fList.append(fileList)

# print(fList)



def statFile(toStat):

    # i is going to be the variable used for each of the metadata elements
    i = os.stat(toStat,follow_symlinks=False)

    # mode
    mode = i[0]

    # inode
    inode = i[1]

    # uid
    uid = i[4]

    # gid
    gid = i[5]

    # file size
    fsize = i[6]

    # access time
    atime = i[7]

    # modification time
    mtime = i[8]

    # ctime => windows is the birth of the file. when it was created
    # unix it is when attributes of the file change.
    ctime = i[9]
    crtime = i[9]

    print("0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(toStat, inode, mode, uid, gid, fsize, atime, mtime, ctime, crtime))

for eachFile in fList:
    statFile(eachFile)

