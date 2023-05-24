#!/usr/bin/python3
"""
N queens
"""

import sys


def safe_positn(board, row, col):
    """
    Check if it's safe to place a queen at the given
    position (row, col) on the chessboard.
    """
    board_size = len(board)

    # Check row on the left side
    for c in range(col):
        if board[row][c] == 1:
            return False

    # Check upper diagonal on the left side
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Check lower diagonal on the left side
    r, c = row, col
    while r < board_size and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1

    return True


def SolveNqueens(board, col, solutns):
    """
    Recursively solve the NQueens problem by placing queens column by column

    Args:
        board (list): The current state of the chessboard.
        col (int): The current column being considered.
        solutns (list): List to store the found solutions.

    Returns:
        bool: True if a solution is found, otherwise False.
    """
    board_size = len(board)

    if col == board_size:
        # Found a solutn, convert board state to coordinates & add to solutns
        solutn = []
        for r in range(board_size):
            for c in range(board_size):
                if board[r][c] == 1:
                    solutn.append([r, c])
        solutns.append(solutn)
        return True

    found = False
    for r in range(board_size):
        if safe_positn(board, r, col):
            # Place a queen at the current position
            board[r][col] = 1
            # Recur for the next column
            found = SolveNqueens(board, col + 1, solutns) or found
            # Backtrack and remove the queen from the current position
            board[r][col] = 0

    return found


def NQueens(n):
    """
    Solve the N Queens problem and print all solutns.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns: None
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solutns = []
    SolveNqueens(board, 0, solutns)

    for solutn in solutns:
        print(solutn)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        NQueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
