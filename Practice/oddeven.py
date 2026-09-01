def isEven(num):
    if num% 2 == 0:
        return True
    else:
        return False

def isOdd(num):
    if num % 2 != 0:
        return True
    else:
        return False

# assert isOdd(42) == False

# assert isOdd(9999) == True

# assert isOdd(-10) == False

# assert isOdd(-11) == True

print(isOdd(3.1415))

print(isEven(42))

# assert isEven(9999) == False

# assert isEven(-10) == True

# assert isEven(-11) == False

# assert isEven(3.1415) == False