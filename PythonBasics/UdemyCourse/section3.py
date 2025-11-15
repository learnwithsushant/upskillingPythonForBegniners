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