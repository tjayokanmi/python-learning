while True:
    try: 
        number = int(input("Enter an integer: "))
        break 
    except ValueError:
        print("Please enter a valid integer.")
def classify_number(number):
    odd_even = ""
    posneg = ""
    if number > 0: 
        posneg = "Positive"
    elif number == 0:
        posneg = "Zero"
    else: 
        posneg = "Negative"

    if number % 2 == 0:
        odd_even = "Even"
    else: 
        odd_even = "Odd"

    return f"{number} is {posneg}\n{number} is {odd_even}"

print(classify_number(number))