from datetime import datetime


def get_birthday_per_week(users):
    current_day =  datetime.now().strftime("%A")
    current_month =  datetime.today().month
    
    birthday_users = {}
    
    for user in users:
        user_name = user['name']
        user_date = user['birthday'].strftime("%A")
        user_month = user['birthday'].month
        if current_month == user_month:
            print(user_date == 'Saturday')
            if user_date == 'Saturday' or user_date == 'Sunday':
                birthday_users['Monday'] = user_name
            # else :
            birthday_users[user_date] = user_name
            # print(user_date)
            
    print(birthday_users)




week_days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Monday',
    7: 'Monday'
    }

    

users = [
    {'name': 'Anna', 'birthday': datetime(1994, 1, 4)},
    {'name': 'Olga', 'birthday': datetime(1991, 2, 11)},
    {'name': 'Danylo', 'birthday': datetime(1989, 4, 29)},
    {'name': 'Natallia', 'birthday': datetime(1981, 8, 8)},
    {'name': 'Denys', 'birthday': datetime(1988, 8, 8)},
    {'name': 'Volodymyr', 'birthday': datetime(1990, 8, 12)},
    {'name': 'Ostap', 'birthday': datetime(1975, 9, 11)},
]


get_birthday_per_week(users)
