def convertToCelsius(fah):
    celsius = (fah - 32) * (5/9)
    return round(celsius, 2)

def convertToFahrenheit(cel):
    fahr = cel * (9/5) + 32
    return round(fahr, 2)

# print(convertToCelsius(0) == -17.77777777777778)

# print(convertToCelsius(180) == 82.22222222222223)

# print(convertToFahrenheit(0) == 32)

# print(convertToFahrenheit(100) == 212)

# print(convertToCelsius(convertToFahrenheit(15)) == 15)

print(convertToFahrenheit(0))
print(convertToFahrenheit(100))
print(convertToCelsius(180))