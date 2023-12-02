import random
print("welcome to the random game:")
number = int(input("enter the number :"))
x = random.randint(1,10)

if number < x :
    print('youre less than this.')
    print('you have another chance to guess it again.')
elif number > x:
    print('your greater than this ')
    print('you have another chance to it ')
else:
    print('congratulation youre are corect')