import random

print("Welcome to the random game:")
number = int(input("Enter the number: "))
x = random.randint(1, 10)

if number < x:
    print('You are less than this.')
    print('You have another chance to guess it again.')
elif number > x:
    print('You are greater than this.')
    print('You have another chance to guess it again.')
else:
    print('Congratulations! You are correct.')
