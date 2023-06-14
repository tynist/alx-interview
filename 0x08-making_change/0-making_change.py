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

    # Initialize the list to store the minimum coin count
    mini_coin = [float('inf')] * (total + 1)
    mini_coin[0] = 0

    # Iterate over each coin value
    for coin_value in coins:
        # Iterate from the coin value to the target total
        for i in range(coin_value, total + 1):
            # Update mini_coin[i]
            mini_coin[i] = min(mini_coin[i], mini_coin[i - coin_value] + 1)

    # Check if the total cannot be met by any combination of coins
    if mini_coin[total] == float('inf'):
        return -1
    else:
        return mini_coin[total]
