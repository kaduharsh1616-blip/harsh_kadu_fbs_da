#Python Program to Remove the Characters of Odd Index Values in a STRING.

str = input("Enter a string: ")
new_str = ""

for i in range(len(str)):
    if i % 2 == 0:
        new_str += str[i]

print("String after removing characters at odd indices:", new_str)
