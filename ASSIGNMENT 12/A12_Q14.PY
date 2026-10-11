# Python Program to count the occurrences of ach word in a string.

str = input("Enter a string: ")
words = str.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Occurrences of each word in the string:")
for word, count in word_count.items():
    print(f"{word}: {count}")


