def calculate_average(numbers):
    total = sum(numbers)
    try:
        return total/len(numbers)
    except ZeroDivisionError:
        # print("This is an empty list")
        return None

print(calculate_average([2,3,4,5]))
print(calculate_average([]))