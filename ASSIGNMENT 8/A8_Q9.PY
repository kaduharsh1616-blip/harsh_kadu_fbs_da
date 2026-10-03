#Write a program to check if entered number is a palindrome or NOT USING FUNCTION 

def is_palindrome(n):
    str_n = str(n)
    cleaned_str = ''.join(c.lower() for c in str_n if c.isalnum())
    return cleaned_str == cleaned_str[::-1]

n = int(input("Enter a number: "))

if is_palindrome(n):
    print(n, "is a palindrome.")
else:
    print(n, "is not a palindrome.")
