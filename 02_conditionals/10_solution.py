pet = input("Enter your pet type: ")
age = int(input("Enter your age: "))

if pet == 'dog':
    if age < 2:
        food = 'Puppy food'
    else:
        food = 'Not available'
elif pet == 'cat':
    if age > 5:
        food = 'Senior Cat food'
    else: 
        food = 'Not available'
else: 
    print("Enter a valid pet.")
    exit()

print(food)