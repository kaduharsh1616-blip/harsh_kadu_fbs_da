# Write a program to check whether a number is prime or not using recursion
def is_prime(n, divisor=None):
    if divisor is None:
        divisor = n - 1

    if n <= 1:
        return False
    elif divisor == 1:
        return True
    elif n % divisor == 0:
        return False
    else:
        return is_prime(n, divisor - 1)
    
n = int(input("Enter a number: "))
if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")