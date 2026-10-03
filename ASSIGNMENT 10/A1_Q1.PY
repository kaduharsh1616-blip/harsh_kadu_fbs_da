# Write a program to find sum of all elements of list
def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

lst = [1, 2, 3, 4, 5]
print("Sum of all elements in the list is:", sum_of_list(lst))
