#more Variables and printing

my_name = "anu"
my_age = 29
my_height = 153
my_weight = 105
my_eyes = "blue"
my_teeth = 'white'
no_of_teeth = 32
my_hair = 'brown'

print("my name is %s and my age is %d" % (my_name, my_age))
print('color of my eyes is %s and color of my hair is %s' %(my_eyes, my_hair))
print(' my height and weight is %d & %d pounds.' %(my_height, my_weight))

print('i have %d number of teeth and all are %s in color' %(no_of_teeth, my_teeth))
total = no_of_teeth+my_weight+my_height+my_age
print(total)

print( 'if I add my age %d, my height %d, my weight %d and my teeth %d' % (my_age, my_height, my_weight, no_of_teeth),'the total will be %d.' %total)
