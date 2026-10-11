#Python Program to Find the Intersection of Two Lists
List1 = [10, 21, 4, 45, 66, 93]
List2 = [1, 3, 5, 7, 9, 11, 21, 45]

intersection_list = list(set(List1) & set(List2))

print("Intersection of Lists:", intersection_list)