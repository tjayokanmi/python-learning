def fizzBuzz(upTo):
    if upTo % 5 == 0 and upTo % 3 == 0:
        print("FizzBuzz", end = "")
    elif upTo % 3 == 0:
        print("Fizz", end = "")
    elif upTo % 5 == 0:
        print("Buzz", end = "")
    else: 
        print(upTo, end = "")
    print()
    

fizzBuzz(390)