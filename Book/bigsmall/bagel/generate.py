import random

def generate_secret():
    digits = []
    for _ in range(3):
        while True:
            gen = str(random.randint(0,9))
            if gen not in digits:
                digits.append(gen)
                break
    secret = digits[0] + digits[1] + digits[2]
    return secret

def get_guess():
    
    while True:
        guess= input("Guess my secret number: ")
        if len(guess) == 3 and guess.isdigit():
            break 
        
    return guess

# print(get_guess())

def evaluate_guess(guess, secret):
    # guess = get_guess()
    # secret = generate_secret()
    result = ""

    for num in range(len(secret)):
        if secret[num] == guess[num]:
            result += "Fermi "
        
        elif secret[num] in guess:
            result += "Pico "

    if result == "":
        result = "bagels"
        
    return result

print(evaluate_guess("123", "123"))
