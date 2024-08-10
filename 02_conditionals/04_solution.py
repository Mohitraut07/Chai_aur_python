# Fruit Ripeness Checker

fruit = input("Enter your fruit: ").lower()
color = input("Enter your fruit color: ").lower()


if fruit == 'banana':
    if color == 'green':
        condition = 'unripe'
    elif color == 'yellow':
        condition = 'ripe'
    elif color == 'brown':
        condition = 'overripe'
    else: 
        print("Enter a valid color")
        exit()
else: 
    print("Enter a valid fruit")
    exit()


print("The Fruit is",condition)