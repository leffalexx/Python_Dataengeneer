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
