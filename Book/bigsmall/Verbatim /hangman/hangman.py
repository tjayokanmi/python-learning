import random, sys

#set up the constants:
#(!) try adding or changing the strings in HANGMAN_PICS to make a 
#guillotine instead of a gallows.
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

#(!) Try replacing CATEGORY and WORDS with new strings.
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()

def main(): 
    print("Hangman, by Al Sweigart")

    #setup variables for a new game:
    missedLetters = [] #List of incorrect letter guesses
    correctLetters = [] #List of correct letter guesses
    secretWord = random.choice(WORDS) #The word the player must guess.

    while True: #Main game loop
        drawHangman(missedLetters, correctLetters, secretWord)

        #Let the player enter their letter guess:
        guess = getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:
            #Add the correct guess to correctLetters:
            correctLetters.append(guess)
