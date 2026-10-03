#Write a program to reverse a given number using recursive function.
def reverse_number(n, reversed_num=0):
    if n == 0:
        return reversed_num
    else:
        return reverse_number(n // 10, reversed_num * 10 + n % 10)

n = int(input("Enter a number: "))
print("Reversed number is:", reverse_number(n))

