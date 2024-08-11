# Find the first non-repeated character

string = input("Enter the string: ")

for i in string:
    if string.count(i)==1:
        print(i)
        break