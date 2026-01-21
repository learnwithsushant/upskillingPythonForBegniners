# Learning if-elseif-else

num = 91

if num>=60 and num<80:
    print("First Class")
elif num>=80 and num<90:
    print("Distinction")
else :
    print('Merit')    


# For Loop
my_list = [1,2,3,4,5,6]

for items in my_list:
    print(items)

sum = 0;
for items in my_list:
    sum+=items

print(sum)

myString = 'I am mindful person'

for letters in myString:
    print(letters)

# THis syntax prints Person as many no. of time as letter in "Positive"
myString = "Positive"
for _ in myString:
    print("Person")

myList = [(1,2),(3,4),(5,6),(7,8)]

for a,b in myList:
    print(a)
    print(b)

d= {"k1":1,"k2":2,"k3":3}

#this prints keys in dictionaries
for ditems in d:
    print(ditems)

for dvals in d.values():
    print(dvals)   

x = 0

while x < 5:
    print(f"Value of x is {x}")
    x+=1
else:
    print(f"Value of x is else {x}")


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

