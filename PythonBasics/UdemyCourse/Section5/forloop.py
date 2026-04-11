my_list = [1,2,3,4,5,6,7,8,9,10]
# for items_in_list in my_list:
#     print(items_in_list)

# for items_in_list in my_list:
#     print("Namaskar")    

for num in my_list:
    if num%2 == 0:
        print(f'Even number is: {num}')
    else :
        print(f'Odd number is: {num}')    


myString  = 'My world is beautiful'        
for letters in myString:
    print(letters)


mytupe = (1,2,3,4,5)
for titems in mytupe:
    print(titems)

listOfTuples = [(1,3),(2,4),(5,7),(6,8)]
for a,b in listOfTuples:
    print(a)
    print(b)

d = {'k1':1,'k2':2,'k3':3}
for key,values in d.items():
    print(key,values)