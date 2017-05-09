# String data type

a =  "Hi, My name is Anuradha"
b = 'i live in Philadelphia'

#Length of the string
print(len(a))
print(len(b))

#Locate character in strings
print(a.index("M"))
print(b.index("P"))

#count the character in string
print(a.count('a'))
print(b.count('i'))

#print part of string
print(a[3:9])
print(b[1:10])

#reverse the string
print(a[::-1])

#convert in upper case
print(a.upper())
print(b.upper())

#convert in lower case
print(a.lower())
print(b.lower())

#concatenate the strings
print(a + b)

#Set Data Type
x = (9, 15, 'd', 's', 'd', 'a', 15, 10)
print(set(x))
#  Print length of set data type
print(len(set(x)))

# DIctionary data type
s = {'name':'anu', 'age': 28, 'bday': 26.09}
print(s['name'])
