# Movie ticket pricing

age = int(input('Enter your age: '))
day = str(input('Enter the day on which you want to watch movie: ')).lower()

week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

# if day in week:
#     if age >= 18:
#         print("Your ticket price is $12.")
#     elif age >= 18 and day == 'wednesday':
#         print("Your ticket price is $10.")
#     elif age < 18 and day == 'wednesday':
#         print("Your ticket price is $6.")
#     else: 
#         print("Your ticket price is $8.")
# else:
#     print("Enter a valid day.")

# More efficient way of writing  code

price = 12 if age >= 18 else 8

if day in week:
    if day == 'wednesday':
        price -= 2
    print("Your ticket price is: $",price)
else: 
    print("Enter a valid day.")