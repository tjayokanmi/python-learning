# stock maps item names to available quantities. 
# order is a list of (item, quantity) pairs. 
# Stock values are non-negative integers; order quantities are integers, not booleans. 
# Keys are strings. These shapes and types are guaranteed.

def reserve_stock(stock, order):
    remaining = stock.copy()
    for item, quantity in order:
        if quantity > stock[item]:
            raise ValueError("Insufficient stock")
        remaining[item] = stock[item] - quantity
    return remaining

# Required behaviour
# Return a new dictionary containing every stock key with its remaining quantity. 
# Never modify stock or order, including when a request fails.
# An item may occur more than once in order. Its combined requested quantity must be reserved. 
# Never allow a negative remaining quantity.
# Raise ValueError for an unknown item, a quantity of zero or less, or insufficient stock. 
# Error message wording is your choice. An empty order returns an equal but separate dictionary.
# You may use try/except with an assertion that fails if ValueError is not raised. 
# Tests must call the function and check a result or failure, not just print it.