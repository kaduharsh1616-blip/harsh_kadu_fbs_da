# Write a program to find the area and perimeter of following figure (Accept length and breadth from user)
# Rectangle

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
