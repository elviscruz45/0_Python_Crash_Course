# if conditions


requested_toppings = ('mushrooms', 'onions', 'pineapple')

a='mushrooms' in requested_toppings

print(a)

# checking if a value is not in a list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'


if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")


#Using multiple elif blocks

age = 12
if age < 4:
    price = 0
if age < 18:
    price = 5
if age < 65: price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")