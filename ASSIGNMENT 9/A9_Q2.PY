#Write a program to check if given number is Armstrong or not using recursive
#function.
def is_armstrong_number(n, num_digits=None):
    if num_digits is None:
        num_digits = len(str(n))
    
    if n == 0:
        return 0
    
    digit = n % 10
    return digit ** num_digits + is_armstrong_number(n // 10, num_digits)

n = int(input("Enter a number: "))
if is_armstrong_number(n):
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")
    