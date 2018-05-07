#!/usr/bin/python3


def Nqueens(argv):
    import sys
    size = int(argv[1])
    board = [[0] * size for i in range(size) for i in range(size)]
    queens(size, board)

def attack(row, col):
    for x in range(size):
        if board[row][col] == 1 or board[x][col] == 1:
            return True
    for x in range(size):
        for y in range(size):
            if (x + y == row + col) or (x - y == row - col):
                if board[x][y] == 1:
                    return True
    return False
def queens(size, board):
    if size == 0:
        return True
    for i in range(size):
        for j in range(size):
            if (not (attack(i, j))) and (board[i][j] != 1):
                if queens(size - 1) == True:
                    return True
                board[i][j] = 0
    return False

if __name__ == "__main__":
    import sys
    Nqueens(sys.argv)
