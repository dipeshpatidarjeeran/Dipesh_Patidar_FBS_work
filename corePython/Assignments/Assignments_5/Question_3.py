"""
    Accept no. of passengers from user and per ticket cost. 
    Then accept age of each passenger and then calculate total amount 
    to ticket to travel for all of them based on following condition :
    a. Children below 12 = 30% discount
    b. Senior citizen (above 59) = 50% discount
    c. Others need to pay full.
"""
ticket_price = int(input("enter the ticket price:-"))
total_amount =0

for i in range (1,6):
    age = int(input(f"enter the age of person_{i} :-"))
    if age<12:
        pay = ticket_price - ticket_price*30/100
        total_amount += pay
        print(f"pay amount is {pay}")
    elif age>59:
        pay = ticket_price - ticket_price*50/100
        total_amount += pay
        print(f"pay amount is {pay}")
    else:
        total_amount += ticket_price
        print(f"pay amount is {ticket_price}")

print(f"total amount for 5 person is {total_amount}")