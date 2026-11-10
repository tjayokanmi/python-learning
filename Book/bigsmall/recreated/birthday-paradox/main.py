import random
import datetime

NUMBER_OF_SIMULATIONS = 100_000

def generate_birthdays(number_of_birthdays):
    
    birthday_dates = []      

    start_date = datetime.date(1991, 1 , 1)

    for _ in range(number_of_birthdays):
        random_days = random.randrange(365)
        generated_date = start_date + datetime.timedelta(days=random_days)
        birthday_dates.append(generated_date)

    return birthday_dates

def check_for_match(birthdays):
    return len(birthdays) != len(set(birthdays))

def run_simulation(number_of_birthdays, number_of_simulations):
    count = 0
    for _ in range(number_of_simulations):
        birthdays = generate_birthdays(number_of_birthdays)
        if check_for_match(birthdays):
            count += 1
    return count 

def calculate_probability(successful_simulations, total_simulations):
    if total_simulations == 0:
        return None
    return round((successful_simulations/total_simulations) * 100, 2)

def get_user_input():
    while True:
        try:            
            num = int(input("Please enter a number between 1 and 100 "))
            if 1 <= num <= 100:
                break
            else:
                print("Please enter a number between 1 and 100")
        except ValueError:
            print("Kindly enter a valid number here")
    
    return num

def display_results(
    number_of_birthdays,
    number_of_simulations,
    successful_simulations,
    probability
):

    print(f"Number of birthdays: {number_of_birthdays}")
    print(f"Number of simulations: {number_of_simulations}")
    print(f"Number of successful simulations: {successful_simulations}")
    print(f"Probability: {probability}%")

def main():
    group_size = get_user_input()
    successful_count = run_simulation(group_size, NUMBER_OF_SIMULATIONS)
    probability = calculate_probability(successful_count,NUMBER_OF_SIMULATIONS)
    display_results(group_size, NUMBER_OF_SIMULATIONS, successful_count, probability)

if __name__ == "__main__":
    main()