#A man goes for shopping. He buys 5 products. Accept the price of all products and display the total cost of shopping. If the total cost is more than 1000 then he will get a discount of 10% on total cost. Display the final amount to be paid by him.
product1 = float(input("Enter the price of product 1: "))
product2 = float(input("Enter the price of product 2: "))
product3 = float(input("Enter the price of product 3: "))
product4 = float(input("Enter the price of product 4: "))
product5 = float(input("Enter the price of product 5: "))

total_cost = product1 + product2 + product3 + product4 + product5

if total_cost > 1000:
    discount = total_cost * 0.10
    final_amount = total_cost - discount
else:
    final_amount = total_cost

print("Final amount to be paid: Rs.", final_amount)