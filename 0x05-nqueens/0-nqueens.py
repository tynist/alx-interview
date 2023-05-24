#!/usr/bin/python3
"""
N queens
"""
import sys


def solve_nqueens(n):
    """
    Solve the N queens problem and return a list of solutions.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        list: A list of solutions, where each solution is represented as a list
              of coordinates [(row1, col1), (row2, col2), ...].
    """

    def is_safe(board, row, col):
        """
        Check if it is safe to place a queen at the given position.

        Args:
            board (list): The current board configuration.
            row (int): The row of the position being checked.
            col (int): The column of the position being checked.

        Returns:
            bool: True if it is safe to place a queen, False otherwise.
        """

        # Check if there is a queen in the same column
        for i in range(row):
            if board[i] == col:
                return False

        # Check if there is a queen in the same diagonal
        for i in range(row):
            if abs(board[i] - col) == abs(i - row):
                return False

        return True

    def place_queens(board, row):
        """
        Recursively place queens on the board starting from the given row.

        Args:
            board (list): The current board configuration.
            row (int): The current row to place a queen.

        Returns:
            None
        """

        if row == n:
            # All queens are placed, add the current board config to solutions
            solutions.append([(i, board[i]) for i in range(n)])
            return

        for col in range(n):
            if is_safe(board, row, col):
                # Place a queen at the current position
                board[row] = col
                # Recursively place queens in the next row
                place_queens(board, row + 1)

    solutions = []
    board = [-1] * n
    place_queens(board, 0)
    return solutions


if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)

    for solution in solutions:
        print(solution)
