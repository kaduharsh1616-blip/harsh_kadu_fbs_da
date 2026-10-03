# Write a program of having n number of elements in the list and find out even
#and odd elements in that list and then create two separate lists which will have
#even elements and other will have odd elements

def separate_even_odd(lst):
    even_list = [num for num in lst if num % 2 == 0]
    odd_list = [num for num in lst if num % 2 != 0]
    return even_list, odd_list

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", lst)
even_numbers, odd_numbers = separate_even_odd(lst)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

