import json
numbers = [2, 3, 5, 7, 11, 13,15,17,19,21,23,25,27,29]
filename = 'numbers.json'

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

