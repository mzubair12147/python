 
# this will automatically open and close the file. so we don't need to do that by ourselves. (convenient, right -_o)
# but it will not catch or handle exceptions that might occur. so we need to do that by ourselves
try:
    with open('./fileToRead.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print("The file do not exists")
else:
    print(file.closed) 