# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

from datetime import datetime

balance = 0
history = []
operation_count = 0
COMISSION = 0.015
MIN_COMISSION = 30
MAX_COMISSION = 600
STEP = 50
iNTEREST_RATE = 1.03
LUXURY_LIMIT = 5000000
TAX_RATE = 0.1


def deposit(amount):
    global balance
    balance += amount
    history.append((datetime.now(), f'Пополнение на {amount} руб.'))
    update_operation_count()


def withdraw(amount):
    global balance
    commission = amount * COMISSION
    commission = max(commission, MIN_COMISSION)
    commission = min(commission, MAX_COMISSION)

    if amount + commission > balance:
        print('Недостаточно средств!')
        return

    balance -= amount + commission
    history.append(
        (datetime.now(), f'Снятие {amount} руб. (комиссия {commission} руб.)'))


def update_operation_count():
    global operation_count
    global balance

    if balance > LUXURY_LIMIT:
        tax = balance * TAX_RATE
        balance -= tax
        print(f'Начислен налог: {tax} руб.')

    operation_count += 1
    if operation_count % 3 == 0:
        print('Начислены проценты')
        balance *= iNTEREST_RATE


def print_balance():
    print(f'Текущий баланс: {balance} руб.')


def print_history():
    for date, operation in history:
        print(date.strftime("%d.%m.%Y %H:%M"), operation)


while True:

    print_balance()

    operation = input(
        'Выберите операцию (1 - пополнить, 2 - снять, 3 - история, 0 - выход): ')

    if operation == '1':
        amount = int(input('Введите сумму пополнения кратную 50 руб.: '))
        if amount % STEP != 0:
            print(f'Сумма должна быть кратна {STEP}!')
            continue
        deposit(amount)

    elif operation == '2':
        amount = int(input("Введите сумму для снятия кратную 50 руб.: "))
        if amount % STEP != 0:
            print(f'Сумма должна быть кратна {STEP}!')
            continue
        withdraw(amount)

    elif operation == '3':
        print_history()

    elif operation == '0':
        print("До свидания!")
        break

print('Ваш баланс:', balance)
