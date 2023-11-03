# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions


import fractions


def fraction_calc(fraction1, fraction2):
    a, b = fraction1.split('/')
    c, d = fraction2.split('/')
    a, b, c, d = int(a), int(b), int(c), int(d)

    sum_numerator = a*d + b*c
    sum_denominator = b*d
    sum_fraction = f'{sum_numerator}/{sum_denominator}'

    mult_numerator = a*c
    mult_denominator = b*d
    mult_fraction = f'{mult_numerator}/{mult_denominator}'

    return sum_fraction, mult_fraction


fraction1 = input('Введите первую дробь в виде a/b: ')
fraction2 = input('Введите вторую дробь в виде c/d: ')

sum_fraction, mult_fraction = fraction_calc(fraction1, fraction2)

print(f'Сумма: {sum_fraction}')
print(f'Произведение: {mult_fraction}')

print('Проверка модулем Fractions: ')

x = fractions.Fraction(1, 7)
y = fractions.Fraction(5, 9)

print(f'Сумма: {x+y}')
print(f'Произведение: {x*y}')
