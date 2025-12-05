import math
print(f"Sqr root {math.sqrt(25)}")
normString = "python"
print(normString[::-1])
reveresedString = "".join(reversed(normString))
print(reveresedString)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = []  # Initialize an empty list to store the results

# Iterate through the lists using their indices
for i in range(len(list1)):
    # Add corresponding elements and append the sum to list3
    list3.append(list1[i] + list2[i])

print(list3)

normString = "madam"
reveresedString = "".join(reversed(normString))
if normString == reveresedString:
    print("Palindrom")

print(f"Sqr root {math.sqrt(25)}")

replaceChar = "This is the perfect time to study gen AI"
print(replaceChar.replace(" ","_"))

strMultiplier = 's'
print(strMultiplier*10)

splitDemo = "Lets split this string"
ll = splitDemo.split()
print(ll)

charCount = 'banana'
print(charCount.count('a'))

print(charCount.index('n'))

print('openai'.upper().lower())

# Swap case

print('Hello Wonderful WorLd'.swapcase())

print('Hello Wonderrful WorLd'.swapcase())

print('programming'.replace('m',""))

word = "programming"
result = word[3:7]
print(result)

new_list = ['a','b','c','e','w','q']
sorted_list = new_list.sort()
print(new_list)
print(sorted_list)

print(new_list.reverse())
print(new_list.count)

#Q12
strRep = 'Hello_everyone'
newStr = strRep.replace('everyone','there')
print(newStr)

#Q13
strRep = "Hello World How are you"
newStr = strRep.replace(' ','-')
print(newStr)

#Q14
withSpaces = ' messy text '
trimSpaces = withSpaces.lstrip().rstrip()
print(trimSpaces)

#Q18
word_list = ["I", "Love", "Coding","Python"]
separator = " "
sentence = separator.join(word_list)
print(sentence)






