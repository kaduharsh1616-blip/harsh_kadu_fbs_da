# Write a program to create a duplicate of an existing list. It should not point to
#same list.
def create_duplicate_list(lst):
    return lst.copy()

lst = [1, 2, 3, 4, 5]
print("Original list:", lst)
print("Duplicate list:", create_duplicate_list(lst))

