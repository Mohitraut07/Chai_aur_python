# Sum of even numbers

num  = int(input("Enter the number: "))

count =0

for i in range(1,num+1):
    if i%2==0:
        count += i

print(count)