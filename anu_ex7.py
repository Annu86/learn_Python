#assigments and Identity

#assigments

a = 10
b  = 5
c = a+b
print(c)

c += a
print(c)
c -= a
print(c)
c *= b
print(c)

c /= b
print(c)
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