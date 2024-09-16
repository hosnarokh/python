from datetime import datetime


def calc_age():
    result = ''
    birthday_date = input()
    date_items = birthday_date.split("/")

    try:
        if (int(date_items[0]) > datetime.now().year or int(date_items[1]) <= 0 or int(date_items[1]) > 13
                or int(date_items[2]) <= 0 or int(date_items[2]) > 32):
            result = 'WRONG'
        else:
            result = datetime.strptime(birthday_date, "%Y/%M/%d")
            if result > datetime.now():
                result = 'WRONG'

            else:
                age = datetime.now().year - result.year
                result = age
    except ValueError:
        result = 'WRONG'
    print(result)


calc_age()
