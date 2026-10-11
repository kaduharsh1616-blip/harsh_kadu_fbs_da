#Python Program to find larger string without using built-in functions.
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Find the length of each string
len1 = 0
for char in str1:
    len1 += 1

len2 = 0
for char in str2:
    len2 += 1

# Compare the lengths
if len1 > len2:
    print("The first string is larger.")
elif len2 > len1:
    print("The second string is larger.")
else:
    print("Both strings have the same length.")