import os

path_to_detect = './demo_folder\\'

# this function will not tell you that it is a file or not
if os.path.exists(path_to_detect):
    print("The file exists")
    if os.path.isfile(path_to_detect):
        print("It is actually a file")
    if os.path.isdir(path_to_detect):
        print("It is actually a directory")
else:
    print("The file do not exists")