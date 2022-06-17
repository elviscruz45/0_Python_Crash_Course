        
filename = 'Pag222.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip() + "hola")
    
    
    
# Working with a File’s Contents

