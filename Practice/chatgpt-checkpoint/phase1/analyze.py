def analyze_numbers(numbers): 
    sum_numbers = sum(numbers)
    largest = max(numbers)
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    
    return f"Sum: {sum_numbers}\nLargest: {largest}\nEven count: {count}"


print(analyze_numbers([3, 8, 2, 5, 10]))
    
