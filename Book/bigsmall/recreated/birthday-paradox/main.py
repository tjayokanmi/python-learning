import random
import datetime

def generate_birthday(number_of_birthdays):
    
    store_dates = []      

    start_date = datetime.date(1990, 1 , 1)

    for i in range(number_of_birthdays):
        random_days = random.randint(0,364)
        generated_date = start_date + datetime.timedelta(days=random_days)
        store_dates.append(generated_date)

        
    return store_dates


birthdays = generate_birthday(5)

print(birthdays)
print(len(birthdays))
print(type(birthdays[0]))