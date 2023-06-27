#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Find the winner of the prime game given the rounds and nums.
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

    def get_prime_numbers(n):
        """
        Get a list of prime numbers up to n.
        Args:
            n (int): The upper limit for generating prime numbers.
        Returns:
            list: List of prime numbers up to n.
        """
        # Create an empty list to store the prime numbers.
        primes = []

        # Iterate over the numbers from 2 to n.
        for number in range(2, n + 1):
            if is_prime_number(number):  # Check if the number is prime.
                primes.append(number)  # add to the list If the number is prime
        return primes

    def can_player_win(primes, n):
        """
        Check if a player can win for a given n.

        Args:
            primes (list): List of prime numbers.
            n (int): The number to check.

        Returns:
            bool: True if the player can win, False otherwise.
        """
        # If n is a prime number, the player can win
        if n in primes:
            return True
        # Otherwise, check if n is divisible by any of the prime numbers.
        for prime in primes:
            if n % prime == 0:
                return True
        # If none of the above conditions are met, the player cannot win
        return False

    # Initialize the count of Maria's & Ben's wins to 0
    maria_wins_count = 0
    ben_wins_count = 0

    # Iterate over the list of numbers
    for i in range(x):
        round_num = nums[i]
        round_primes = get_prime_numbers(round_num)
        if can_player_win(round_primes, round_num):
            # If Maria can win, increment Maria's win count
            maria_wins_count += 1
        else:
            # If Ben can win, increment Ben's win count
            ben_wins_count += 1

    # Return the name of the player with the most wins.
    if maria_wins_count > ben_wins_count:
        return "Maria"
    elif ben_wins_count > maria_wins_count:
        return "Ben"
    else:
        return None
