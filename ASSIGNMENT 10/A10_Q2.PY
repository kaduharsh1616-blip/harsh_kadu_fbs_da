# Write a program to find maximum and minimum element in a list
def find_max_min(lst):
    if not lst:
        return None, None  # Return None for both if the list is empty
    max_num = lst[0]
    min_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num

lst = [1, 2, 3, 4, 5]
max_element, min_element = find_max_min(lst)
print("Maximum element in the list is:", max_element)
print("Minimum element in the list is:", min_element)
