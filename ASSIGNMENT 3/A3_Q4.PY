### WAP TO INPUT ALL SIDES OF TRIANGLE IS VALID OR NOT 

side1 = int(input('enter the first side:'))
side2 = int(input('enter the second side:'))
side3 = int(input('enter the third side:'))

if(side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2):
    print('the triangle is valid:')
else:
    print('the triangle is not valid:')
