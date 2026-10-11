# Python Program to Detect if Two Strings are Anagrams

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")   

if sorted(str1) == sorted(str2):
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")

    