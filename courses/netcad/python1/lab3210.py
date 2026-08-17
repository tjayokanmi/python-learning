# Prompt the user to enter a word
user_input = input("Enter a word: ")
# and assign it to the user_word variable.
user_word = user_input.upper()
for letter in user_word:
    # Complete the body of the for loop.
    if letter not in ["A", "E", "I", "O", "U"]: 
        print(letter)
    else: 
        continue

