# Function returning multiple values
import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = math.pi * radius * 2
    return area, circumference

a, c = circle_stats(2)

print("Area:",a,"Circumference:",c)