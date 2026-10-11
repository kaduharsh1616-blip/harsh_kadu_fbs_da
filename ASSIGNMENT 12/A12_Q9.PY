#Python Program to Calculate the Number of Words and the Number of
#Characters Present in a String.
str = input("Enter a string: ")
words = str.split()
num_words = len(words)
num_chars = len(str)
print("Number of words in the string:", num_words)
print("Number of characters in the string:", num_chars)
