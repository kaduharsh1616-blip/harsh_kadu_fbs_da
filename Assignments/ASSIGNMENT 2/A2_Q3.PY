#CONVERT FEET AND INCHES INTO CENTIMETER AND ,METER

## INPUT

feet=int(input('enter the value of feet:'))
inches=int(input('enter the value of inches:'))

meter=(feet*0.3048)+(inches*0.0254)
centimeter=(feet*30.48)+(inches*2.54)

print('meter:',meter)
print('centimeter:',centimeter)