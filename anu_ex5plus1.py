#more Variables and printing

print('*'*25)
my_name = "anu"
my_age = 29
my_height = 153
my_weight = 105
my_eyes = "blue"
my_teeth = 'white'
no_of_teeth = 32
my_hair = 'brown'
# %s is used to substitute string variable or data type and %d is used for numeric data type

print("my name is %s and my age is %d" % (my_name, my_age))
print('color of my eyes is %s and color of my hair is %s' %(my_eyes, my_hair))
print(' my height and weight is %d & %d pounds.' %(my_height, my_weight))

print('i have %d number of teeth and all are %s in color' %(no_of_teeth, my_teeth))
total = no_of_teeth+my_weight+my_height+my_age
print(total)

print( 'if I add my age %d, my height %d, my weight %d and my teeth %d' % (my_age, my_height, my_weight, no_of_teeth),'the total will be %d.' %total)

# %s & %d can also be used for direct print without assigning variable

print('*'*25)
print('my age is %s.' % 'twenty nine')
print ('my age is %d.' % 29)

print('*'*25)
#more printing

print('marry had a', 'littile lamb '* 2)
print('.'*10)

end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

print (end1 + end2 + end3 + end4 + end5 + end6),
print (end7 + end8 + end9 + end10 + end11 + end12)
print('*'*25)

# error: Cheese Burger didn't appear in same line ( as per website it was in same line)