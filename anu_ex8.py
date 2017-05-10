# Membership and Bitwise Operators

#Membership in and not in

a = 14
b=10
list = [11, 12, 14, 15, 16, 17]

print('a is present in the list:', a in list)
print('b is present in the list:', b in list)

if(a in list):
    print('a is present in the list')



if(b not in list):
    print('b is not in the list')

#Bitwise Operators

a =  10
b = 13
c = a&b # Binary AND
print(c)
d = a|b # Binary OR
print(d)
e = a^b # Binary XOR
print(e)
#f = a ~ b # Binary Not
#print(f)
g = a<<1  # Binary Left Shift
print(g)
h = b>>1  # Binary Right Shift
print(h)