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
    queens = generate_queens()
    if seminar_6.chess.check_valid(queens):
        print(queens)
