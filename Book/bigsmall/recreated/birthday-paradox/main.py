import random
import datetime

def generate_birthdays(number_of_birthdays):
    
    store_dates = []      

    start_date = datetime.date(1991, 1 , 1)

    for i in range(number_of_birthdays):
        random_days = random.randint(0,364)
        generated_date = start_date + datetime.timedelta(days=random_days)
        store_dates.append(generated_date)

        
    return store_dates

def check_for_match(birthdays):
    # length_of_list = len(birthdays)
    # set_birthdays = set(birthdays)
    # length_of_set = len(set_birthdays)

    return len(birthdays) != len(set(birthdays))

    # if length_of_list == length_of_set:
    #     return False
    # return True

def run_simulation(number_of_birthdays):
    count =  0

    for i in range(100000):
        check_for_match(number_of_birthdays)
        if check_for_match = True:
            count += 1
    return count 