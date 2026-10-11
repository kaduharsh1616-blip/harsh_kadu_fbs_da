#Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged
str = input("Enter a string: ")

new_str = str[-1] + str[1:-1] + str[0]
print("String after exchanging the first and last characters:", new_str)
