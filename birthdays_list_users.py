from collections import defaultdict
from datetime import datetime
from pprint import pprint
from random import randint
from typing import Dict, List


def get_weekday_by_id(weekday_id: int):
    weekday_map: Dict[int,str] = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    return weekday_map[weekday_id]


def generate_date() -> datetime.date:

    month_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
    year = randint(1970, 2015)
    month = randint(1, 12)
    day = randint(1, month_days[month])
    return datetime(year=year, month=month, day=day).date()
    

users_birthdays: List[Dict[str, datetime.date]] = [
    {
        'username 1': generate_date(),
        'username 2': generate_date(),
        'username 3': generate_date(),
    },
    {
        'username 4': generate_date(),
        'username 5': generate_date(),
        'username 6': generate_date(),

    },
    {
        'username 7': generate_date(),
        'username 8': generate_date(),
        'username 9': generate_date(),
    },
]


def construct_current_date(day_of_birth: datetime.date):
    current_year = datetime.now().year
    return datetime(year=current_year, month=day_of_birth.month, day=day_of_birth.day).date()


def get_birthdays_per_week(users: List[Dict[str, datetime]]):

    greeting_scheduler: Dict[str, List] = defaultdict(list)

    for user_dict in users:
        for username, birthday in user_dict.items():
            current_year_birthday = construct_current_date(birthday)
            birthday_day_index = current_year_birthday.weekday()
            weekday = get_weekday_by_id(birthday_day_index)
            if weekday in ['Sunday', 'Saturday']:
                weekday = 'Monday'
            greeting_scheduler[weekday].append(username)
    pprint(dict(greeting_scheduler))
    return greeting_scheduler


if __name__ == '__main__':
    
    get_birthdays_per_week(users_birthdays)
