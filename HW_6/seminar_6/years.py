# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

def _check_leap(year: int) -> bool:
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

def  is_exist_date(date: str) -> bool:
    day, month, year = (int(el) for el in date.split("."))
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    if month == 2 and day > 29:
        return False
    if month == 2 and day == 29 and not _check_leap(year):
        return False
    return True


__all__ = ["is_exist_date"]


if __name__ == "__main__":
    print(is_exist_date("24.22.4563"))