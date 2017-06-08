# now we will try raw_input and argv together

from sys import argv

script, user_name = argv
prompt = '> '

print("Hi %s, I am the %s script:" % (user_name, script))
print("I'd like to ask you a few questions")
print('Do you like me? % s' % (user_name))
likes = input(prompt)

print('Where do you live? % s' % (user_name))
lives = input(prompt)

print("how many computer do you have %s" % (user_name))
computer = input(prompt)
