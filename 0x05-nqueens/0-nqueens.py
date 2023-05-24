#!/usr/bin/python3
"""
N queens
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens_util(board, col, solutions):
    """
    A recursive utility function to solve the N Queens problem.
    """
    if col == len(board):
        # Found a solutn, convert board state to coordinates & add to solutns
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place a queen at board[i][col]
            board[i][col] = 1
            # Recur for the next column
            res = solve_nqueens_util(board, col + 1, solutions) or res
            # Backtrack and remove the queen from board[i][col]
            board[i][col] = 0

    return res


def solve_nqueens(n):
    """
    Solve the N Queens problem and print all solutions.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        None
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        solve_nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
