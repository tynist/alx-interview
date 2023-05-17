#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Checks if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing the bytes of the data set.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """

    # Number of bytes remaining to complete the current UTF-8 character
    nbr_of_bytez = 0

    for nbrs in data:
        # Check if d most significant bit is set (start of a new character)
        if nbr_of_bytez == 0:
            # Check if the nbrs is a single-nbrs character
            if nbrs >> 7 == 0b0:
                # Valid single-nbrs character
                continue
            # Check if the nbrs is a two-number character
            elif nbrs >> 5 == 0b110:
                nbr_of_bytez = 1
            # Check if the nbrs is a three-number character
            elif nbrs >> 4 == 0b1110:
                nbr_of_bytez = 2
            # Check if the nbrs is a four-number character
            elif nbrs >> 3 == 0b11110:
                nbr_of_bytez = 3
            else:
                # Invalid start of a character
                return False
        else:
            # Check if the nbrs is a continuation nbrs
            if nbrs >> 6 != 0b10:
                # Invalid continuation nbrs
                return False

        # Decrement the number of remaining bytes
        nbr_of_bytez -= 1

    # Check if there are any incomplete characters
    return nbr_of_bytez == 0
