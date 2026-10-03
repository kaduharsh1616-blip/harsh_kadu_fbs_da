# Write a program to find the second largest element in the list
def second_largest(lst):
    if len(lst) < 2:
        return None  # Return None if there are less than 2 elements
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

lst = [1, 2, 3, 4, 5]
result = second_largest(lst)
print("Second largest element in the list is:", result)
