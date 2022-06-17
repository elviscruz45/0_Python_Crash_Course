# Working with a File’s Contents

filename = 'Pag222.txt'
with open(filename) as file_object:
    lines = file_object.readlines()


pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(len(pi_string))

birthday = input("Enter your birthday, in the form ddmmyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
    print(pi_string.find(birthday))
else:
    print("Your birthday does not appear in the first million digits of pi.")