# WAP to check if a given number is Armstrong number or not. For
#each task create separate functions.
def is_armstrong_number(n):
    str_n = str(n)
    num_digits = len(str_n)
    sum_of_powers = sum(int(digit) ** num_digits for digit in str_n)
    return sum_of_powers == n

n = int(input("Enter a number: "))
if is_armstrong_number(n):
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")
    