myfile = open('PythonBasics\\UdemyCourse\\Resources\\myFile.txt')
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())