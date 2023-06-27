#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determine the winner of each game given the number of rounds and the list of numbers.
    Args:
        x (int): Number of rounds to play.
        nums (list of int): A list of the numbers rolled in each round.
    Returns:
        str: Name of player that won most rounds.
        None: If no winner.
    """

    def is_prime_number(number):
        """
        Determines if a number is prime.
        Args:
            number (int): The number to check.
        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if number < 2:  # Numbers less than 2 are not prime
            return False
        for i in range(2, int(number ** 0.5) + 1):
            # Check divisibility of the number from 2 to its square root
            if number % i == 0:
                # Not prime if divisible by any value
                return False
        return True  # Number is prime if no divisor is found

    player_1_wins = 0
    player_2_wins = 0

    # Iterate over the list of numbers
    for n in nums:
        # Count the number of primes between 2 and n
        primes_count = sum(
            1 for num in range(2, n + 1) if is_prime_number(num)
        )
        if primes_count % 2 == 0:
            # If the count of primes is even, Ben wins
            player_2_wins += 1
        else:
            # If the count of primes is odd, Maria wins
            player_1_wins += 1

    # Return the winner of the game
    if player_1_wins > player_2_wins:
        return "Maria"  # Maria wins if she has more wins
    elif player_2_wins > player_1_wins:
        return "Ben"  # Ben wins if she has more wins
    else:
        return None  # No winner in case of a tie
