# Counting Positive Numbers

numbers = [1,-2,1,-2, -2,-5,-3,2,2,4,5,4,-6,5,-45,7,5,-4]
positive_number_count = 0

for num in numbers:
    if num > 0: positive_number_count+= 1

print("Total positive count is: ",positive_number_count)