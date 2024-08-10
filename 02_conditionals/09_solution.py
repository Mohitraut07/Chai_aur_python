# Leap year Checker

year = int(input("Enter your year: "))

if (year % 4 ==0 and year % 100 != 0)or year % 400 ==0:     
    year_type = "Leap"
else:
    year_type = "Not leap"

print(year_type)