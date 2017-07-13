#assigments and Identity

#assigments

a = 10
b  = 5
c = a+b
print(c)

# += operand adds the last value of c with a
c += a
print(c)
# -= operand subtract the last value of c with a
c -= a
print(c)
# *= operand multiply the last value of c by b
c *= b
print(c)
# /= operand divide the last value of c by b
c /= b
print(c)
# **= operand make b as the power of the last value of c
c **= b
print(c)

# Identity

x = 12
y = 12

if ( x is y):
    print('y is present in x')
z = 15
if (x is not z):
    print('x is not present in z')