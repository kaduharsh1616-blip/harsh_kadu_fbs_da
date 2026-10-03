#WAP to print Armstrong number within a given range

num1 = int(input("Enter the starting number of the range: "))
num2 = int(input("Enter the ending number of the range: "))

print(f"Armstrong numbers between {num1} and {num2} are:")

for num in range(num1, num2 + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)