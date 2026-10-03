# Write a program to remove all occurrences of a given element in the list
def remove_occurrences(lst, element):
    return [num for num in lst if num != element]

lst = [1, 2, 3, 4, 5, 3, 6, 3, 7]
element = 3
print("Original list:", lst)
print("List after removing all occurrences of", element, ":", remove_occurrences(lst, element)) 

