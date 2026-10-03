#Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
#b. 1!+ 2! + 3! + 4!+..... + n!
#c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def factorial(k):
    result = 1
    for i in range(2, k + 1):
        result *= i
    return result


def sum_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total


def sum_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total


n = int(input("Enter n: "))

print("a. 1 + 2 + ... + n      =", sum_natural(n))
print("b. 1! + 2! + ... + n!   =", sum_factorials(n))
print("c. 1^1 + 2^2 + ... + n^n =", sum_powers(n))

