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

