#Write a program to remove duplicates from the list
def remove_duplicates(lst):
    return list(set(lst))

lst = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", lst)
print("List after removing duplicates:", remove_duplicates(lst))

