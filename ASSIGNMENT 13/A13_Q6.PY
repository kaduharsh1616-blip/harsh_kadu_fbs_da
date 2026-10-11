#Python Program to Multiply All the Items in a Dictionary

my_dict = {'a': 10, 'b': 20, 'c': 30}


total = 1
for value in my_dict.values():
    total *= value
    
print(f"The product of all the items in the dictionary is: {total}")