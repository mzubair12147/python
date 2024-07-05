with open('fileToWrite.txt','a') as file:
    file.write("Suck my cock bitch\n")
print(file.closed)

with open('fileToWrite.txt') as file:
    print(file.read())
print(file.closed)