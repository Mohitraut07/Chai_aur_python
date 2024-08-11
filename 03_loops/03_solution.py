# Multiplication Table Printer
# Skip for 5
num = int(input("Enter the multiplicant: "))

for i in range(1,11):
    if i != 5:
        print(num,'*',i,"=",i*num)