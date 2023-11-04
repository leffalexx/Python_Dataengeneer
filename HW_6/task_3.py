# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей
# в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random
import seminar_6.chess


def generate_queens():
    queens = []
    while len(queens) < 8:
        x = random.randint(0, 7)
        y = random.randint(0, 7)

        if (x, y) not in queens:
            queens.append((x, y))

    return queens


for i in range(4):
    random_queens = generate_queens()
    if seminar_6.chess.check_valid(random_queens):
        print(random_queens)
