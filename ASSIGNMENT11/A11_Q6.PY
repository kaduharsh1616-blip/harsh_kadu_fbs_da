#Python Program to Find the Union of two Lists
List1 = [10, 21, 4, 45, 66, 93]
List2 = [1, 3, 5, 7, 9, 11]

union_list = list(set(List1) | set(List2))

print("Union of Lists:", union_list)