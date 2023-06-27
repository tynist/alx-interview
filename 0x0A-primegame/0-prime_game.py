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
    if not nums or x < 1:
        return None

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

    def count_primes_up_to(n):
        """
        """
        # Create an empty list to store the prime numbers.
        primes = []

        # Iterate over the numbers from 2 to n.
        for number in range(2, n + 1):
            if is_prime_number(number):  # Check if the number is prime.
                primes.append(number)  # add to the list if number is prime
        return len(primes)

    # Number of rounds Maria & Ben has won.
    maria_wins_count = 0
    ben_wins_count = 0

    # Iterate over the list of numbers
    for n in nums:
        # Count the number of primes up to n.
        prime_count = count_primes_up_to(n)
        # If the number of primes is odd, Maria wins the round.
        if prime_count % 2 == 1:
            maria_wins_count += 1
        else:
            # Otherwise, Ben wins the round.
            ben_wins_count += 1

    # Return the name of the player with the most wins.
    if maria_wins_count > ben_wins_count:
        return "Maria"
    elif ben_wins_count > maria_wins_count:
        return "Ben"
    else:
        return None
