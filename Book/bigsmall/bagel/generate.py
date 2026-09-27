import random

def generate_secret():
    digits = []
    for _ in range(3):
        while True:
            gen = random.randint(0,9)
            gen =str(gen)
            if gen not in digits:
                digits.append(gen)
                break
    # print(list)
    secret = digits[0] + digits[1] + digits[2]
    return secret