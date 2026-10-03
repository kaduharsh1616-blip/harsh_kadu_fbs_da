# Write a program to reverse the list
def reverse_list(lst):
    return lst[::-1]

lst = [1, 2, 3, 4, 5]
print("Original list:", lst)
print("Reversed list:", reverse_list(lst))