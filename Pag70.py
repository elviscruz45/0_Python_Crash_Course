bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

print(bicycles[-1])

#apending elements to the end of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

#insert

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#Removing an Item using the del Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[2]
print(motorcycles)


#Removing an item using a pop() method

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#Popping items from any Position in a List
print("----------------Popping items from any Position in a List-----------------")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles.pop(0))


#Removing an Item by Value
print("----------------Removing an Item by Value-----------------")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)

#Sorting a list permanently with the sort() method
print("----------------Sorting a list permanently with the sort() method-----------------")

cars = ['bmw', 'audi', 'toyota', 'subaru'] 
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)


#Sorting a list permanently with the sort() method
print("----------------Sorting a list permanently with the sort() method-----------------")

cars = ['bmw', 'audi', 'toyota', 'subaru'] 
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Sorting a list temporarily with the sorted() function
print("----------------Sorting a list temporarily with the sorted() function-----------------")

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

#printing a list in reverse order

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)


# Finding the Length of a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)