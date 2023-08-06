import random

print("Hello Fat Man")
date = 24
month = "June"

time = 4
print("The current month and day is", month, date-1)
computer_is_on = True
if computer_is_on:
    print("Yes, the computer is on")
else:
    print("No, the computer is not on")
weight = 188.3
height = 60
if weight <= 180:
    print("You're on track")
else:
    print(weight, "pounds")
    print("Lose some weight fat-man")

lucky_number = random.randint(1, 75)

print(f'Your lucky number is: {lucky_number}') 

magic_number = random.randint(1, 3)

if magic_number == 1:
    print('Yes, today is your lucky day')
if magic_number == 2:
    print('Today may be a lucky day')
if magic_number == 3:
    print('Today is not a good day for you, just stay in bed')
    
print('Now, move on to lists...')

fav_numbers = [21, 13, 44]
print(fav_numbers)

fav_numbers.append(99)
print(fav_numbers)

fav_numbers.insert(0, 105)
print (fav_numbers)

del(fav_numbers[2])
print(fav_numbers)

for number in range (40):
    print((number+1)*2)
    
for x in fav_numbers:
    print(x)
    
    


