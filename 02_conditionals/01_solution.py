# Age group categorization program 

age = int(input("Enter your age: "))

# if age< 13:
#     print("You are a Child.")
# elif age>=13 and age<=19:
#     print("You are a Teenager.")
# elif age>=20 and age<=59:
#     print("You are an Adult.")
# else:
#     print("You are a Senior.")

# More sensible way of writing
if age< 13:
    print("You are a Child.")
elif age<20:
    print("You are a Teenager.")
elif age<60:
    print("You are an Adult.")
else:
    print("You are a Senior.")