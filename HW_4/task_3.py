# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
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
COMMISSION = 0.015
MIN_COMMISSION = 30
MAX_COMMISSION = 600
STEP = 50
INTEREST_RATE = 1.03
LUXURY_LIMIT = 5000000
TAX_RATE = 0.1


def deposit(deposit_amount):
    global balance
    balance += deposit_amount
    history.append((datetime.now(), f'Пополнение на {deposit_amount} руб.'))
    update_operation_count()


def withdraw(withdraw_amount):
    global balance
    commission = withdraw_amount * COMMISSION
    commission = max(commission, MIN_COMMISSION)
    commission = min(commission, MAX_COMMISSION)

    if withdraw_amount + commission > balance:
        print('Недостаточно средств!')
        return

    balance -= withdraw_amount + commission
    history.append(
        (datetime.now(), f'Снятие {withdraw_amount} руб. (комиссия {commission} руб.)'))


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
        balance *= INTEREST_RATE


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
        print('До свидания!')
        break

print('Ваш баланс:', balance)
