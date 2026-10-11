#Python Program to Take in Two Strings and Display the Larger String
#without Using Built-in Functions
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

length1 = 0
for char in str1:
    length1 += 1

length2 = 0
for char in str2:
    length2 += 1

if length1 > length2:
    print("The larger string is:", str1)
elif length2 > length1:
    print("The larger string is:", str2)
else:
    print("Both strings have the same length.")