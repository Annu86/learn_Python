# Data type
# List data type
task = ['brush', 'bath', 'breakfast', 'office', 'Gym']
print(task)

# update your list
task[1] = 'dry clean'
print(task)

#print length of the list  "counting starts from index 0, index 1, index 2....
print(len(task))

#print an element of the list
print(task[3])
print(task[0])

# print part of the list  (as the counting starts from index 0, so if we say 0:3, printing will start from index 0 to index 2, it will not include 3.)
print(task[0:3])
print(task[1:5])

# Concatenation of the lists
list1 = ['dinner',  'drinks', 'sleep']
print(task + list1)

# print list multiple times
print((task+list1)*2)

#Tuple data type
#define a tuple
task1 = ('physics','chemistry','maths','biology')
print(task1)

#check whether tuple data type can be update or not
#task1[2] = 'computer science'    (it will show error )

#print length of the list
print(len(task1))

#print an element of the Tuple
print(task1[1])

# print part of the Tuple
print(task1[1:3])

# Concatenation of the Tuples
task2 = ('hindi', 'IT', "English", 'total', 7 )
print(task1+task2)

# print Tuple multiple times
print(task1*3)



