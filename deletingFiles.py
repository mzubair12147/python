import os
import shutil
file_path = './fileToDelete.txt'
folder_path = './directoryToRemove\\'
# note: The remove function do not delete empty folders
# note: the rmdir function do not delete the folders that have some files.
try:
    os.rmdir(folder_path)
    # os.remove(file_path)
    # note: rmtree is a dangerous function because it will delete the folder and all of the files inside it.
    # shutil.rmtree(folder_path)
except FileNotFoundError:
    print("The file is not found")
except PermissionError:
    print("You do not have persmission to delete an empty folder")
except OSError:
    print("You cannot delete the folder, because it is not empty")
else:
    print(f"{folder_path} was deleted")

