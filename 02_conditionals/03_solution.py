# Grade Calculator

score = int(input("Enter your score: "))

# if score>=90 and score<100:
#     print("Your Grade is: 'A'")
# elif score>=80 and score<90:
#     print("Your Grade is: 'B'")
# elif score>=70 and score<80:
#     print("Your Grade is: 'C'")
# elif score>=60 and score<70:
#     print("Your Grade is: 'D'")
# else:
#     print("Your Grade is: 'F'")

# More efficient way to write code
if score >=90:
    grade = 'A'
elif score >=80:
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else: 
    grade = 'F'

if score >= 101:
    print('Enter a valid score.')
    exit()

print("Your grade is:",grade)