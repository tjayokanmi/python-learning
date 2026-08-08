"""Bagels, by Al Sweigart al@inventwithpython.com
 A deductive logic game where you must guess a number based on clues.
 View this code at https://nostarch.com/big-book-small-python-projects
 A version of this game is featured in the book "Invent Your Own
 Computer Games with Python" https://nostarch.com/inventwithpython
 Tags: short, game, puzzle"""

 import random 

 NUM_DIGITS = 3 # (!) Try setting this to 1 or 10.
 MAX_GUESSES = 10 #(!) Try setting this to 1 or 100.

 def main():
    print("""Bagels, a deductive logic game.
     By Al Sweigart al@inventwithpython.com
    
     I am thinking of a {}-digit number with no repeated digits.
     Try to guess what it is. Here are some clues:
     When I say:    That means:
     Pico         One digit is correct but in the wrong position.
     Fermi        One digit is correct and in the right position.
     Bagels       No digit is correct.
     
     For example, if the secret number was 248 and your guess was 843, the
     clues would be Fermi Pico.""")

     while True: 
        #create the secret number. 
        secret_num = get_secret_num()

        print("I have thought up a number.")
        print(f"You have {MAX_GUESSES} guesses to get it.")

        num_guesses = 1

        while num_guesses <= MAX_GUESSES:
            guess = ""

            #Keep asking untill a valid guess is entered.
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guesses}:")
                guess = input("> ")

            clues = get_clues(guess, secret_num)
            print(clues)

            if guess == secret_num:
                break

            num_guesses += 1
        if num_guesses > MAX_GUESSES:
            print("You ran out of guesses.")
            print(f"The answer was {secret_num}.")
        
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
        
    print("Thanks for playing!")

def get_secret_num(): 
    """Return a string made of unique random digits."""
    numbers = list("0123456789")
    random.shuffle(numbers)

    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += numbers[i]

    return secret_num


def get_clues(guess, secret_num): 
    """Return the clues for the player's guess."""

    if guesses