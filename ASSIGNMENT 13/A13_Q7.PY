#Python Program to Remove the Given Key from a Dictionary

my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

key_to_remove = 'age'

if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"The key '{key_to_remove}' has been removed from the dictionary.")
else:
    print(f"The key '{key_to_remove}' does not exist in the dictionary.")

