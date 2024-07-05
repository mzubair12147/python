'''
    copyfile() : copy contents of a file
    copy() : copyfile() + permission mode + destination can be a directory
    copy2() : copy() + copies meta data (file's creation and modification time)
'''

import shutil

shutil.copy2('fileToRead.txt', dst= './copyDestination/copiedFile2.txt')