### a program to calculate profit or loss.

sellingprice= int(input('enter the sellingprice:'))
costprice=int(input('enter the costprice:'))

profit = sellingprice - costprice
loss = costprice - sellingprice

if(sellingprice > costprice):
    print('profit')
else:
    print('loss')
