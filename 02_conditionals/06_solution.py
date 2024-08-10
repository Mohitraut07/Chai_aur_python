# Transportation Mode Selection

distance = int(input("Enter the travel distance: "))

if distance < 3:
    mode = 'Walk'
elif distance > 3:
    mode = 'Bike'
elif distance > 15:
    mode = 'Car'
else:
    print("Enter valid distance.")

print(mode)