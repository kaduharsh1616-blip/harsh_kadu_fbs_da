# Write a program to create a new list from existing list which contains cube of
#each number of list.
def create_cube_list(lst):
    return [x**3 for x in lst]

lst = [1, 2, 3, 4, 5]
print("Original list:", lst)
print("List with cubes:", create_cube_list(lst))




