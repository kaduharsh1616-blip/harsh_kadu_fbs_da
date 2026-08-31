###to check whether the triangle is equilateral isosceles or scalenetriangle
side1 = int(input('enter the first side:'))
side2 = int(input('enter the second side:'))
side3 = int(input('enter the third side:'))
if(side1 == side2 == side3):
    print('the triangle is equilateral:')
elif(side1 == side2 or side2 == side3 or side1 == side3):
    print('the triangle is isosceles:')
else:
    print('the triangle is scalene:')