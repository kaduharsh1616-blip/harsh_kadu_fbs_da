#Write a program to find sum of following series using recursive functions:
#i. 1! + 2! + 3! + 4! +..... + n!
#Note : For fact and sum two recursive functions 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_of_factorials(n):
    if n == 0:
        return 0
    else:
        return factorial(n) + sum_of_factorials(n - 1)

n = int(input("Enter a number: "))
print("Sum of factorials from 1 to", n, "is:", sum_of_factorials(n))