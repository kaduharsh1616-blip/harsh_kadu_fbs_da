### Accept age of five people and also per person ticket amount and then calculate total
##amount to ticket to travel for all of them based on following condition
##a. Children below 12 = 30% discount
##b. Senior citizen (above 59) = 50% discount
##c. Others need to pay full price

ticket_price = int(input("Enter ticket price per person: "))

total_amount = 0

for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))
    
    if age < 12:
        # Children below 12 get 30% discount
        amount = ticket_price * 0.7
    elif age > 59:
        # Senior citizens above 59 get 50% discount
        amount = ticket_price * 0.5
    else:
        # Others pay full price
        amount = ticket_price
    
    total_amount += amount

print("Total ticket amount for all 5 people:", total_amount)





    

