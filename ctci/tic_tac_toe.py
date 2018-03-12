#!/usr/bin/env python3

# ctci 16.4

def threqual(x):
    if x[0] in ('1', '2') and x[0] == x[1] == x[2]:
        return True
    return False


def check_parallel(board, transpose = False):
    if transpose:
        order = [7, 4, 1, 8, 5, 2, 0, 6, 3]
        board = [board[x] for x in order]

    sequences = board[0:3], board[3:6], board[6:9]
    for seq in sequences:
        print('checking', seq)
        if threqual(seq):
            return True
    return False


def check_diagonal(board):
    dd = board[0], board[4], board[8]
    du = board[6], board[4], board[2]

    if threqual(dd) or threqual(du):
        return True

    return False


def won(board):
    if check_parallel(board):
        return True

    if check_parallel(board, True):
        return True

    if check_diagonal(board):
        return True

    return False

