for i in range(1,5):
    print(i)
    

#Using range() to make a list of numbers
listas=list(range(0,102,2))
print(listas)

#Simple statistics with a list of numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8,   0]


print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehension

square=[i**2 for i in range(1,10) if i%2==0]

print(square)


#working with Part of list

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])
print(players[-3:])


players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
    
# Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]