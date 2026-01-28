for num in range(10):
    print(num)

for num in range(7,10):
    print(num)   

#with step size

for num in range(0,11,2):
    print(num)  

#with enumerator

word = 'abcde'
for item in enumerate(word):
    print(item)

for index,letter in enumerate(word):
    print(index)
    print(letter)

# zip function

zipList1=[1,2,3,4]


zipList2=['a','b','c','d']
zipList3=[3.1,3.2,3.3,3.4]

for item in zip(zipList1,zipList2,zipList3):
    print(item)

zipList4 = list(zip(zipList1,zipList2,zipList3))

print(zipList4)

print('a' in 'a world')
print('mykey' in {'mykey':1})

d= {'mykey':1}
print(1 in d.values())
print(1 in d.keys())

listWithmin=[1,2,3,4]

print(min(listWithmin))

print(max(listWithmin))

from random import shuffle

myShhuffleList = ['ABC','efg','xyz','def','msd']

shuffle(myShhuffleList)

from random import randint

print(randint(1,100))

strLetters = "IamDeveloper"
lettersList = [letter for letter in strLetters]
print(lettersList)
numList = [x for x in range(10,100)]
print(numList)
sqnumList = [x**2 for x in range(1,10)]
print(sqnumList)
oddListNum = [x for x in range(10,100) if x%2!=0]
print(oddListNum)

# celcius to farenheit
celcius = [10,23,44,55,65]
farenheit = [((9/5)*temp+32) for temp in celcius]
print(farenheit)

# if-else in flattern list
oddListNum = [x if x%2!=0 else 'Even' for x in range(0,13)]
print(oddListNum)

#nested loop in flattern list
nestedListLoop = [x*y for x in range(0,10,2) for y in range(0,10,1)]
print(nestedListLoop)