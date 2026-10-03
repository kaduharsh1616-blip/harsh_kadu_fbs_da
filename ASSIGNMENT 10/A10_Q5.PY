# Accept a number from user and check if this element is present in the list or
#not. Also tell how many times it is present in the list
lst = [1, 2, 3, 4, 5]
num = int(input("Enter a number to search in the list: "))
if num in lst:
    count = lst.count(num)
    print(f"Number {num} is present in the list {count} times.")
else:
    print(f"Number {num} is not present in the list.")
    