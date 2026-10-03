#Write a program to calculate area of circle USING FUNCTION
import math

def calculate_area(radius):
    return math.pi * radius ** 2

radius = 5
area = calculate_area(radius)
print(f"The area of the circle is: {area}")