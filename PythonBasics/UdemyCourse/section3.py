# String format operation

print('String using formating will be used here -- > {} squeezed within'.format("Here i am"))

print("I am the {2} {0} in this {1}".format("person","world","luckiest",))

print("I am the {m} {p} in this {u}".format(p="person",u="universe",m="mindful",))

# Fomating with floating point no.

divs= 100/888;
print(divs)

print("Formated floating point no. is {r:1.3f}".format(r=divs))

print(f"Formated floating point no. is {divs:1.4f}")

mlist = ['one','two','three']
print(mlist)
mlist[0] = 'ONE'
print(mlist)
mlist.append("four")
print(mlist)

myFirstDist = {"key1":"value1","key2":"value2","key3":"value3"}
print(myFirstDist)
print(myFirstDist["key2"])

price_lookUp = {"apple":5,"banana":15,"grapes":20}
print(price_lookUp["grapes"])

#Nested Dictionaries
nested_Dictionary = {"k1":"VW","k2":15,"k3":["SPM","AbV","KHS"],"k4":{"CBSE":["SPM","KHS"],"SSC":["AbV","SPM","MSG","HSC"]}}
print(nested_Dictionary)
print(nested_Dictionary["k2"])
print(nested_Dictionary["k3"][-1])
print(nested_Dictionary["k4"]["SSC"][-2])
nested_Dictionary["k4"]["SSC"].append("NIS")
print(nested_Dictionary)
print(nested_Dictionary.keys())


def get_all_keys(d):
    keys = []
    for key, value in d.items():
        keys.append(key)
        if isinstance(value, dict):     # check if nested dictionary
            keys.extend(get_all_keys(value))
    return keys

all_keys = get_all_keys(nested_Dictionary)
print(all_keys)


print(nested_Dictionary.values())

print(nested_Dictionary.items())

# Startting  with Tuples
t1=(1,2,3,4,5,6,7)
print(t1.count(1))
print("Index of element 7 is -> ",t1.index(7))
print("Index of element 6 is -> ",t1.index(6))
print("Index of element 2 is -> ",t1.index(2))
print("Index of element 1 is -> ",t1.index(1))
