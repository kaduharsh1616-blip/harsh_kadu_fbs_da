# Write a program find reverse of a number USING FUNCTION
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

n = int(input("Enter a number: "))
print("Reverse of", n, "is:", reverse_number(n))