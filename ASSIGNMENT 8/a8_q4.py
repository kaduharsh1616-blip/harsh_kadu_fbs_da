#Sum of all odd numbers between 1 to n using function
def sum_odd_numbers(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total

n = int(input("Enter n: "))
print("Sum of odd numbers between 1 to", n, "is:", sum_odd_numbers(n))