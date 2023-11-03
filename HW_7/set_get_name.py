# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Получите имена и сохраните их в файл.


from pathlib import Path
from random import randint, choice

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LEN = 4
MAX_LEN = 7

def gen_name():
    name = ''
    fl = randint(0, 1)
    for i in range(randint(MIN_LEN, MAX_LEN)):
        if (i + fl) % 2 != 0:
            name += choice(CONSONANTS)
        else:
            name += choice(VOWELS)
    return name.title()


def set_name(count: int, file: str | Path) -> None:
    with open(file, 'a', encoding='utf-8') as f:
        for _ in range (count):
            print(gen_name(), file=f)


if __name__ == '__main__':
    set_name(120, Path('names.txt'))
