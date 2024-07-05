import os

source = './directoryToMove\\'
destination = './moveDestination\\directoryToMove' 


# to move file
try:
    if os.path.exists(destination):
        print("There is already a file there.")
    else:
        os.replace(source,destination)
        print("The file moved successfully")
except FileNotFoundError as e:
    print("File not found")


# to move folder
try:
    if os.path.exists(destination):
        print("There is already a folder there.")
    else:
        os.replace(source,destination)
        print("The folder moved successfully")
except FileNotFoundError as e:
    print("folder not found")
