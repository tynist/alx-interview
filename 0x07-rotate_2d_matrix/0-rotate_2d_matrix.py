#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees in a clockwise direction.

    Args:
        matrix (list): The matrix to be rotated

    Returns:
        None. The matrix is modified in-place.
    """
    n = len(matrix)

    # Perform matrix transpose
    for i in range(n):
        for j in range(i, n):
            # Swap elements along the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row of the transposed matrix
    for i in range(n):
        # Use slicing to reverse the row
        matrix[i] = matrix[i][::-1]
