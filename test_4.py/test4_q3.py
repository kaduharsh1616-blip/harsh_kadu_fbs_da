#


width = 22

print("*" * width)

for i in range(1, 11):
    print(" " * (width - i * 2) + "*")

print("*" * (width - 1) + "*")
