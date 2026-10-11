#Print 1 to 100 in snakes and ladder pattern.
for i in range(1, 101):
    if i % 10 == 0:
        print(i)
    elif (i // 10) % 2 == 0:
        print(i, end=' ')
    else:
        print(101 - i, end=' ')