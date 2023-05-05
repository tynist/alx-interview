#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.

    Args:
    - n: an integer representing the desired number of H characters in the file

    Returns:
    - an integer representing the minimum number of operations needed to achieve
    n H characters, or 0 if it is impossible to achieve n H characters

    """

    # If n is less than 1, it is impossible to achieve n H characters, so return 0
    if n < 1:
        return 0
    
    # Initialize variables
    current = 1
    clipboard = 0
    count = 0

    # Loop while current is less than n
    while current < n:
        
        # If n is divisible by current, copy all characters to the clipboard and
        # paste them until current equals n
        if n % current == 0:
            clipboard = current
            count += 2
        
        # If n is not divisible by current, paste the clipboard and
        # add the number of characters in the clipboard to current
        else:
            current += clipboard
            count += 1

    # Return the minimum number of operations needed
    return count

