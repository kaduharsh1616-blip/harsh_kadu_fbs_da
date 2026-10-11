#Python Program to Find the Second Largest Number in a List Using Bubble SORT

List1 = [10, 21, 4, 45, 66, 93]
n = len(List1)

# Bubble Sort
for i in range(n):
    for j in range(0, n - i - 1):
        if List1[j] > List1[j + 1]:
            List1[j], List1[j + 1] = List1[j + 1], List1[j]

print("Second Largest Number:", List1[n - 2])