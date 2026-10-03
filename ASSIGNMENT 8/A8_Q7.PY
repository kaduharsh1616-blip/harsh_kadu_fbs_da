#Write  a program to find sum of digits of a number USING FUNCTION 
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

n = int(input("Enter a number: "))
print("Sum of digits of", n, "is:", sum_of_digits(n))