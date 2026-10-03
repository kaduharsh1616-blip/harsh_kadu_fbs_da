# Write a program to reverse a number using recursion
def reverse_number(n):
    if n < 10:
        return n
    else:
        return int(str(n % 10) + str(reverse_number(n // 10)))

n = int(input("Enter a number: "))
print("Reverse of", n, "is:", reverse_number(n))

