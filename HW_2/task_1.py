# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX_LETTER_OFFSET = 87  # для заглавных букв константа 55


def decimal_to_hex(dec_num):
    hex_num = ''
    while dec_num > 0:
        hex_digit = dec_num % 16
        if hex_digit < 10:
            hex_digit = str(hex_digit)
        else:
            hex_digit = chr(hex_digit + HEX_LETTER_OFFSET)
        hex_num = hex_digit + hex_num
        dec_num = dec_num // 16

    return hex_num


decimal_num = int(input('Введите целое число: '))
print(decimal_to_hex(decimal_num))
print(hex(decimal_num))
