word_without_vowels = ""

# Prompt the user to enter a word
user_word = input("Enter a word: ").upper()
# and assign it to the user_word variable.


for letter in user_word:
    if letter in ["A", "E", "I", "O", "U"]:
        continue
    else: 
        word_without_vowels += letter
    # Complete the body of the loop.

print(word_without_vowels)
# Print the word assigned to word_without_vowels.

