# Reverse a string using a loop

string = input("Enter your string: ")
reversed_string = ""

# With loop
for char in string:
    reversed_string = char + reversed_string

print(reversed_string)

# Without loop
# print(string[::-1])

