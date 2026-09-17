# import random

# print("")

# count = 0

# while count < 6:
#     secret_num = random.randint(1, 10)
#     print("Guess the secret number")
#     guess = int(input())
#     if secret_num > guess:
#         print("Number is bigger")
#     elif secret_num < guess:
#         print("Number is smaller")
#     else: 
#         break
#     count += 1

# if guess == secret_num:
#     print(f'Good Job! You have guessed my number in {count}' )
# else: 
#     print(f'Nope. The number I was thinking is {secret_num}')


# This is a guess the number game. 

import random 

print("hello, What is your name")
name =input()
secretNumber = random.randint(1,20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20')

#Ask the player to guess 6 times

for guessTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessTaken) + ' guesses!')
else: 
    print("Nope. The number I was thinking of was " + str(secretNumber)) 