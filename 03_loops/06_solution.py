# Factorial Calculator
# Using while

num = int(input('Enter the factorial number: '))
fact = 1

while(num >0):
    fact = fact * num
    num -= 1

print(fact)