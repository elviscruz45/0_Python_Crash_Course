#Checking that a list is not empty

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Using Multiples Lists

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")


#Dictionaries

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Removing Key-Value Pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)


# A Dictionary of Similar Obkects

favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
print("Sarah's favorite language is " + favorite_languages['sarah'].title() +".")

# key and Values

user_0 = {'username': 'efermi',
              'first': 'enrico',
              'last': 'fermi',}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
    
print(user_0.items())
print(user_0.keys())
print(user_0.values())


user = {'username', 'efermi',
              'first', 'enrico',
              'last', 'fermi',}


# A list of DIctionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
    
    

# A list in a Dictionary

pizza = {'crust': 'thick','toppings': ['mushrooms', 'extra cheese'],}
print("You ordered a " + pizza['crust'] + "-crust pizza " +"with the following toppings:")
for topping in pizza['toppings']: print("\t" + topping)


# How the imput() function works

message = input("Tell me something, and I will repeat it back to you: ")
print(message)