import random

def generate_secret():
    digits = []
    for _ in range(3):
        while True:
            gen = str(random.randint(0,9))
            if gen not in digits:
                digits.append(gen)
                break
    secret = "".join(digits)
    return secret

def get_guess():
    
    while True:
        guess= input("Guess my secret number: ")
        if len(guess) == 3 and guess.isdigit():
            break 
        
    return guess

#evaluate functions
def evaluate_guess(guess, secret):
    
    
    result = []

    for num in range(len(secret)):
        if secret[num] == guess[num]:
            result.append("Fermi")
        
        elif guess[num] in secret:
            result.append("Pico")

    if result == []:
        result.append("bagels")
    
    
    return " ".join(result)

# This is the main function, where everything is connected.
def main():
    while True:
        secret = generate_secret()
        print("For this game, you have only 10 guesses")
        count_guess = 1

        while count_guess < 11: 
            guess = get_guess()
            print(evaluate_guess(guess, secret))
            if guess == secret:
                print("You have guessed correctly")
                break
            
            count_guess += 1

        else:
            print(f"You are out of guesses, the correct number is {secret}")

        print("Do you want to play again? (yes/no)")
        
        while True:
            option = input()
            option = option.upper()
        
            if option == "NO":
                print("Thanks for playing!")
                return
            elif option == "YES":
                print("Here is another chance")
                break
            else:
                print("Kindly enter Yes/No")
main()
