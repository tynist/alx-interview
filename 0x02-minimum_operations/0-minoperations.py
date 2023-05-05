#!/usr/bin/python3
"""Minimum operations"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in
    exactly n H characters in a file.

    :param n: The number of H characters to achieve
    :return: The fewest number of operations needed to achieve
    n H characters, or 0 if n is impossible to achieve
    """
    # If n is less than or equal to 1, no operations are needed
    if n <= 1:
        return 0

    # Iterate over possible operations from 2 to n
    for poss_operations in range(2, n+1):
        # If n is divisible by the operation, 
        # recursively calculate the minimum number of operations needed
        if n % poss_operations == 0:
            return minOperations(int(n/poss_operations)) + poss_operations

    # If there is no possible operation to achieve n, return 0
    return 0
