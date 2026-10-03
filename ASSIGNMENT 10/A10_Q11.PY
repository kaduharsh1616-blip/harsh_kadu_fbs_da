# Write a program to print all numbers which are divisible by m and n in the LIST
def divisible_by_m_and_n(lst, m, n):
    return [num for num in lst if num % m == 0 and num % n == 0]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m = 2
n = 3
print("Original list:", lst)
print("Numbers divisible by", m, "and", n, ":", divisible_by_m_and_n(lst, m, n))


