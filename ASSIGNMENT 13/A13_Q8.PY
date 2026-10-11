#Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

text = "This is a sample text. This text is for testing the frequency of words in this text."

words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")   

    