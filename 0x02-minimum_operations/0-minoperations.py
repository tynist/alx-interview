#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.

    Args:
        n (int): The desired number of H characters in the file.

    Returns:
        int: The fewest number of operations needed to achieve the
        desired number of H characters.
        If impossible to achieve, returns 0.
    """
    # If n is less than 1, it is impossible to achieve
    if n <= 1:
        return 0

    i = 2
    factor = 2
    while i <= n:
        if n % i == 0:
            n = n // i
            factor = i
        else:
            i += 1
    return factor + minOperations(n)
