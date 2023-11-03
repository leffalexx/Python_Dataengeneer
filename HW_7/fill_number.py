# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число Int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000б максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.


from pathlib import Path
from random import randint, uniform

MIN_NUM = -1000
MAX_NUM = 1000


def fill_number(count: int, file: str | Path) -> None:
    with open(file, 'a', encoding = 'utf-8') as f:
        for _ in range(count):
            num_int = randint(MIN_NUM, MAX_NUM)
            num_float = uniform(MIN_NUM, MAX_NUM)
            f.write(f'{num_int}|{num_float}\n')


if __name__ == '__main__':
    fill_number(128, Path('new_numbers.txt'))
