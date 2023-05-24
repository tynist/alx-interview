#!/usr/bin/python3
"""
N queens
"""
import sys


if __name__ == "__main__":

    '''
    If the user called the program with the
    '''
    if not len(sys.argv) == 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not (sys.argv[1]).isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)


def BoadOk(board, row, column, N):

    '''
    Checks if a queen can be placed on the board
    Returns:
        True if queen could be placed
        False if there is not a save place
    '''

    for i in range(column):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1),
                    range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1),
                    range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def SolutionNQ(board, column, N):

    '''
    solves the n queen problem using Backtracking
    by finding the posibles board to placed all the n queens on it
    in a save places
    Returns:
        True if all the queens are placed on the board
        False if a queen can not be placed
    '''

    if column == N:
        Board(board)
        return True

    f = False
    for i in range(N):
        if BoadOk(board, i, column, N):
            board[i][column] = 1
            f = SolutionNQ(board, column + 1, N) or f
            board[i][column] = 0
    return f


def Board(board):

    '''
    prints the row and column where the queens are
    positioned. "Our Board"
    '''

    solve = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solve.append([i, j])
    print(solve)


board = [[0 for i in range(N)] for j in range(N)]
SolutionNQ(board, 0, N)
