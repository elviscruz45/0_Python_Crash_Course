with open('Pag222.txt') as file_object:
    contents = file_object.read()
    print(contents)




filename = 'Pag222.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())