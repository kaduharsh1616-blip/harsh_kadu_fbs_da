##WAP to check if given number Strong Number.
n=int(input("Enter a number: "))
def factorial(num):
    fact=1
    for i in range(1, num+1):
        fact*=i
    return fact