myfile = open('PythonBasics\\UdemyCourse\\Resources\\myFile.txt')
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())

with open('PythonBasics\\UdemyCourse\\Resources\\myFile.txt') as myNewFile:
    contents = myNewFile.read()

    print(contents)

with open('PythonBasics\\UdemyCourse\\Resources\\myFile.txt',mode='a') as myNewWFile:
    myNewWFile.write('\n This new line writen in write mode')
    myNewWFile.write('\n This second line writen in write mode')
    print(myNewWFile)    