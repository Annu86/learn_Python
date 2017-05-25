print('I will count my pens')

print('gel pen =', 10 + 5)
print(' ball pen =', 10+6-3*2)

print('Total pens are gel + ball pen =', 10+5+10+6-3*2)

# lets do some algebraic equations

a = 10+6*9+4-15+200/10
print(int(a))
# in algebraic equations, Python follows PEMDAS rule

#lets do some more algebra

print('what is 8+9 =', 8+9)

print('is it true 5+7 is greater than 5-7?')
print(5+7>5-7)
print (5+7 < 5-7)

l = 10
m = 20
n = 5
print('Is l greater than m?', l>m)
print(" Is m is greater than n?", m>n)
print('Is l is less than or equal to m?', l<=m)
print ('Is l is greater than or equal to n?', l>=n)

# error or something that i don't know
x = 20.55
y = 20.91
z = 20.50

print((x + y))
print(x - z)

# by jai
floating_point_values = 0.5
print ("%0.1f" % (floating_point_values))
print ("%0.11f" % (floating_point_values))
print ("%0.01f" % (floating_point_values))
print ("%0.011f" % (floating_point_values))

print("%0.1f" %(x - z))
print("%0.11f" %(x - z))
print("%0.01f" %(x - z))
print(float(x - z))
print()
# Python stores floats with 'bits', and some floats you just can't represent accurately, no matter how many bits of
# precision you have. This is the problem you have here. It's sorta like trying to write 1/3 in decimal with a limited
#  amount of decimals places perfectly accurate.

floating_point_values = 0.05
print ("%0.1f" % (floating_point_values))
print ("%0.11f" % (floating_point_values))
print ("%0.01f" % (floating_point_values))
print ("%0.011f" % (floating_point_values))
print ("%0.00f" % (floating_point_values))
print ("%0.001f" % (floating_point_values))
print ("%0.010f" % (floating_point_values))


# here's after all experiments
print ("%0.2f" % (x - z))
print ("%0.3f" % (x - z))
