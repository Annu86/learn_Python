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

# use %r for getting debugging information about something.
# The %r will give you the "raw programmer's" version of variable, also known as the "representation."

formatter = ("%r %r %r %r %r")
print(formatter % (1,2,3,4,5))
print(formatter % ('one','two','three','four','five'))
print(formatter % (True, False, True, False, True))
print(formatter %( formatter, formatter, formatter, formatter, formatter))
print(formatter % ('Hi,', "my name is anu.", 'I am learning Python.', 'I like it.', ' I am enjoying it.'))
print('*'*25)

# some more printing
# |n is used to start new line

days = "Sun Mon Tue Wed Thur Fri Sat "
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print('Days in a week are:', days)
print('Months in a year are:', months)

#lets try three double quotes """

print("""I wanna see how it works. 
It looks somthing different. 
Lets see how it results""")
# with three quotes, we can easily print sentences in different lines without wrting print many times
print('*'*25)
#  \ (backslash) character encodes difficult-to-type characters into a string.
# Let's see how

print("I went to \"Qubec City\" last summer")
print(' I\'am gonna live my dream' )
fat_cat = """ I'll do a list:
 \t*cat food
 \t*fishies
 \t*catnip\n\t*grass"""
print(fat_cat)

print('*'*25)