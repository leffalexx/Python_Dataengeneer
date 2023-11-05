# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import datetime


def check_date(date_to_check):
    today = datetime.date.today()

    try:
        date = datetime.datetime.strptime(date_to_check, '%Y-%m-%d').date()

    except ValueError:
        return False

    if date == today:
        return True
    else:
        return False


if __name__ == '__main__':
    test_date = '2023-11-05'
    print(check_date(test_date))
