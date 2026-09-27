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

