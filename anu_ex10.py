from sys import argv
script, file_name = argv
txt = open(file_name)

print("here is your file %s" %file_name)
print(txt.read())

print("type the file name again:")
file_again = input('> ')
txt_again = open(file_again)

print(txt_again.read())