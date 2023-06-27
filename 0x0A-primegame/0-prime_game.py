#!/usr/bin/python3
"""
Prime Game
"""


def is_prime_numbers(n):
    """
    Returns prime numbers between 1 and n using the sieve of Eratosthenes.
    Args:
        n (int): The upper limit to generate prime numbers.
    Returns:
        list of int: Prime numbers between 1 and n.
    """
    prime_numbs = []  # List to store the prime numbers
    # Boolean list to mark all numbers as prime (Sieve of Eratosthenes)
    sieve = [True] * (n + 1)

    # Iterate over the numbers from 2 to n
    for num in range(2, n + 1):
        if sieve[num]:  # If number is marked as prime, adds to the list
            prime_numbs.append(num)
            # Mark all multiples of the current number as non-prime
            for i in range(num, n + 1, num):
                sieve[i] = False
    return prime_numbs  # Return the list of prime numbers


def isWinner(x, nums):
    """
    Determines the winner of the prime game given the rounds and numbers.
    Args:
        x (int): Number of rounds to play.
        nums (list of int): A list of the numbers rolled in each round.
    Returns:
        str: The name of the player that won the most rounds.
        None: If no winner can be determined.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    # Number of rounds Maria & Ben has won
    maria_wins_count = 0
    ben_wins_count = 0

    # Iterate over the list of numbers
    for n in range(x):
        # Get the list of prime numbers for the number `nums[n]`
        prime_numbs = is_prime_numbers(nums[n])
        # If the length of primes is odd, Maria wins the round
        if len(prime_numbs) % 2 != 0:
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
