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
WORDS = 'AARDVARK ADDER ANT ANTELOPE BABOON BADGER BAT BEAR BEAVER BUFFALO BUSHBABY CAMEL CAT CHIMPANZEE CLAM COBRA COUGAR COYOTE CRANE CROCODILE CROW DEER DOG DONKEY DUCK EAGLE ELEPHANT FERRET FOX FROG GOAT GOOSE GORILLA GUENON HAWK HIPPOPOTAMUS HOG HYENA JACKAL LEOPARD LION LIZARD LLAMA MANATEE MANGABEY MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PANGOLIN PARROT PATAS PIGEON PORCUPINE PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WARTHOG WATERBUCK WEASEL WHALE WOLF WOMBAT ZEBRA'.split()


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

            #check if the player has won:
            foundAllLetters = True #start off assuming they've won.
            for secretWordletter in secretWord:
                if secretWordletter not in correctLetters:
                    #There is a letter in the secret word that isn't 
                    #yet in correctLetters, so the player hasn't won:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print("Yes! The secret word:," secretWord)
                print("You have won!")
                break #Break out of the main game loop.
        else:
            #The player has guessed incorrectly:
            missedLetters.append(guess)

            #Check if player has guessed too many times and lost. (The
            #"- 1" is because we don't count the empty gallows in
            #HANGMAN_PICS.)
            if len(missedLetters) == len(HANGMAN_PICS)  - 1:
                drawHangman(missedLetters, correctLetters,  secretWord)
                print('You have run out of guesses!')
                print('The word was "{}"'.format(secretWord))
                break
        

def drawHangman(missedLetters, correctLetters, secretWord):
    """Draw the current state of hangman, along with the missed and correctly-guessed letters of the secret word."""
    print(HANGMAN_PICS[len(missedLetters)])
    print('The category is:', CATEGORY)
    print()

    #show the incorrecty guessed letters:
    print('Missed letters: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    if len(missedLetters) == 0:
        print('No missed letters yet.')
    print()

    #Display the blanks for the secret word (one blank per letter):
    blank = ['_'] * len(secretWord)

    #Replace blanks with correctly guessed letters:
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blank[i] = secretWord[i]
    
    #show the secret word with spaces in between each letter:
    print(' '.join(blanks))