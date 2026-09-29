# A ticket should cost 7 units. The developer expects three tickets to produce the integer 21.
def ticket_total(price, quantity):
    total = price * quantity
    return total
    
amount = ticket_total(7, 3)
print(amount)