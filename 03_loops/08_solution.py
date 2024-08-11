# Check whether a number is prime or not

is_prime = True
num = int(input("Enter your number: "))

if num >1:
    for i in range(2,num):
        if num % i ==0:
            is_prime = False
            break
else: 
    print("Enter a valid number.")

print(is_prime)