#Python Program to Put Even and Odd elements of a List into two Different LISTS.
List1 = [10, 21, 4, 45, 66, 93]
even_list = []
odd_list = []

for num in List1:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even elements:", even_list)
print("Odd elements:", odd_list)
