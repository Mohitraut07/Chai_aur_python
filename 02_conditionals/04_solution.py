# Fruit Ripeness Checker


color = input("Enter your fruit color: ").lower()

if color == 'green':
    condition = 'unripe'
elif color == 'yellow':
    condition = 'ripe'
elif color == 'brown':
    condition = 'overripe'
else: 
    print("Enter a valid color")
    exit()

print("The Fruit is",condition)