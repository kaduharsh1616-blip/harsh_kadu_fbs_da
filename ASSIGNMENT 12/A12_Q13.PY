#Python Program to count number of digits and letters in a string.

str = input("Enter a string: ")
num_digits = 0

num_letters = 0

for char in str:
    if char.isdigit():
        num_digits += 1
    elif char.isalpha():
        num_letters += 1

print("Number of digits in the string:", num_digits)
print("Number of letters in the string:", num_letters)