#Python Program to Concatenate Two Dictionaries Into One

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

concatenated_dict = {**dict1, **dict2}

print(concatenated_dict)

