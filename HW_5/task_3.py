# Создайте функцию генератор чисел Фибоначчи


def fibonacci_numbers():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


fib_generator = fibonacci_numbers()
for i in range(10):
    print(next(fib_generator))
