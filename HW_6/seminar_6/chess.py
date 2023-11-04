board = [[0] * 8 for _ in range(8)]
mock = []


def check_valid(queens):
    for queen in queens:
        x, y = queen
        if board[x][y] == 1:
            return False
        board[x][y] = 1

    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                for k in range(8):
                    if i != k and board[k][j] == 1:
                        return False
                    if j != k and board[i][k] == 1:
                        return False

    for queen in queens:
        x, y = queen
        for k in range(1, 8):
            if (x + k < 8) and (y + k < 8) and board[x + k][y + k] == 1:
                return False
            if (x - k >= 0) and (y - k >= 0) and board[x - k][y - k] == 1:
                return False
            if (x + k < 8) and (y - k >= 0) and board[x + k][y - k] == 1:
                return False
            if (x - k >= 0) and (y + k < 8) and board[x - k][y + k] == 1:
                return False

    return True


if __name__ == "__main__":
    print(check_valid(mock))
    for row in board:
        print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]}')