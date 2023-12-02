import random
numb = int(input("enter the number : "))
wahid = random.randint(1,10)
if wahid > numb:
    print('youre gusess is high')
elif wahid == numb:
    print('welldone, your correct')
else:
    print('you are less than the targeted value ')