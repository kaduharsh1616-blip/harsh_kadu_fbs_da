# Python Program to Calculate the Length of a String Without Using a
#Library Function

str = input("Enter a string: ")
length = 0

for char in str:
    length += 1

print("Length of the string:", length)