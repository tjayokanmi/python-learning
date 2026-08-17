secret_word = "chupacabra"
#guess = input("Guess the word: ")

while True: 
    guess = input("Guess the word: ")
    if secret_word == guess:
        break
    
print("You've successfully left the loop.")