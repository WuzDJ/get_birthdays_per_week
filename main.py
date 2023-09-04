from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    #returns empty dict, if income list is empty
    if not users:
        return {}
    
    days_of_week = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    users_date = date.today()
    
    result_dict = {}
    #it fills the result_dict with values 
    #if user calls function on Friday result will be {'Friday': [], 'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': []}
    for i in range(0,7):
        day_of_week = (users_date.weekday() + i) % 7
        if day_of_week in (5, 6):
            day_of_week = 0
        result_dict.setdefault(days_of_week.get(day_of_week), [])

    next_week = timedelta(days=7)
    next_week = users_date + next_week

    for user in users:
        name = user.get("name")
        birth_date = user.get("birthday")
        this_birth_day = datetime(users_date.year, birth_date.month, birth_date.day)
        next_birth_day = datetime(users_date.year+1, birth_date.month, birth_date.day)

        bool_this_birth_day = (this_birth_day.date() < users_date or next_week < this_birth_day.date())
        bool_next_birth_day = (next_birth_day.date() < users_date or next_week < next_birth_day.date())

        #it skips dates that not interesting for us
        if bool_this_birth_day and bool_next_birth_day:
            continue
        
        #it handles this_birth_day
        if not bool_this_birth_day:
            day_of_week = days_of_week.get(this_birth_day.weekday())
            if day_of_week in ("Saturday", "Sunday"):
                day_of_week = "Monday"
            for key, value in result_dict.items():
                if key == day_of_week:
                    value.append(name)
                    break
        
        #it handles next_birth_day
        if  not bool_next_birth_day:
            day_of_week = days_of_week.get(next_birth_day.weekday())
            if day_of_week in ("Saturday", "Sunday"):
                day_of_week = "Monday"
            for key, value in result_dict.items():
                if key == day_of_week:
                    value.append(name)
                    break
    
    #it dels "empty days" from result_dict
    del_list = []
    for key, value in result_dict.items():
        if not value:
            del_list.append(key)
    
    for key in del_list:
        result_dict.pop(key)

    return result_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
