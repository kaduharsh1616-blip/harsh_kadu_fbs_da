#Write a program to find factorial of given number using recursion

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter a non-negative integer: "))
print(f"{number}! = {factorial(number)}")
