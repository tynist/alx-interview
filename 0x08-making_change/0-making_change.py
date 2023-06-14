#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet the given amount total.

    Args:
        coins (list): List of the values of the coins available.
        total (int): The amount of money you need to make change for.

    Returns:
        int: Fewest number of coins needed to meet the total.
             -1 - If total cannot be met by any combination of coins you have.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for the greedy algorithm
    coins.sort(reverse=True)

    count = 0  # Number of coins used so far
    for coin in coins:
        if coin <= total:
            # Add the maximum number of coins possible for the current denomination
            count += total // coin
            # Update the total by taking the remainder after using the coins
            total %= coin
        if total == 0:
            break

    if total == 0:
        return count  # Successfully made change for the given amount
    else:
        return -1  # Unable to make change for the given amount
