#Python Program to Remove the nth Index Character from a Non-Empty STRING
str = input("Enter a string: ")

n = int(input("Enter the index of the character to remove: "))

new_str = str[:n] + str[n+1:]
print("String after removing the character at index", n, ":", new_str)
