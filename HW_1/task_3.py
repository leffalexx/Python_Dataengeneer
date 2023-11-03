# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint


TRY = 10
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
quiz = randint(LOWER_LIMIT, UPPER_LIMIT)


print(f'Загадано число от {LOWER_LIMIT} до {UPPER_LIMIT}. У Вас есть {TRY} попыток угадать ')
for i in range(TRY):
    guess = int(input('Введите число: '))
    if guess == quiz:
        print('Поздравляю, вы угадали число!')
        break
    elif guess < quiz:
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')


if guess != quiz:
    print(f'Вы не угадали число. Было загадано число {quiz}')
