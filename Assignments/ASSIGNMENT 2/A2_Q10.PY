##to calculate the  intger amount for user 

# take input
amount = int(input('enter amount:'))


# perform operation
notes2000 = amount // 2000
amount = amount % 2000

notes500 = amount // 500
amount = amount % 500

notes200 = amount // 200
amount = amount % 200

notes100 = amount // 100
amount = amount % 100




# desplay result
print('notes2000',notes2000)
print('notes500',notes500)
print('notes200',notes200)
print('notes100',notes100)
