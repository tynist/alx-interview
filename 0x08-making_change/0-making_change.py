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

    coin_count = 0  # Number of coins used so far
    for coin_value in coins:
        if coin_value <= total:
            # Add the max possible coins for the current denomination
            coin_count += total // coin_value
            # Update the total by taking the remainder after using the coins
            total %= coin_value
        if total == 0:
            break

    if total == 0:
        return coin_count  # Successfully made change for the given amount
    else:
        return -1  # Unable to make change for the given amount
