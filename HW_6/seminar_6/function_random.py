# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа:
# нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных
# границах и пользователь должен угадать его за
# заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если
# попытки исчерпаны - ложь.

from random import randint
from sys import argv

__all__ = ["game"]
def game(lower: int=0, upper: int=100, tries:int=10) -> bool:
    num = randint(lower, upper)
    for i in range(tries):
        answer = int(input(f"Введите число от {lower} до {upper}: "))
        if answer > num:
            print(f"Ваше число {answer} больше загаданного")
        elif answer < num:
            print(f"Ваше число {answer} меньше загаданного")
        else:
            print(f"Вы угадали. Загадано число {num}")
            return True
    return False

if __name__ == "__main__":
    name, *param = argv

    print(game(*(int(n) for n in param)))
