#Python Program to count number of lowercase characters in a string.

str = input("Enter a string: ")
count = 0

for char in str:
    if char.islower():
        count += 1

print("Number of lowercase characters in the string:", count)