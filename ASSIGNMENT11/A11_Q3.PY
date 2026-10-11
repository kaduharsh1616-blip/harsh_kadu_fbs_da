#Python Program to Sort the List According to the Second Element in Sublist.
List1 = [[1, 2], [3, 1], [5, 0], [4, 3]]

List1.sort(key=lambda x: x[1])

print("Sorted List:", List1)
