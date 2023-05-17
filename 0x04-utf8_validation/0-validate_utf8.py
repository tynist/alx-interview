#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Checks if a list of integers represents a valid UTF-8 encoding

    Args:
        data (list): List of integers representing the bytes of the data set.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    nbrs_of_bytez = 0  # Number of bytes in the current UTF-8 character

    for nbr in data:
        # Convert the number to its binary representation
        binary_rep = format(nbr, '#010b')[-8:]

        if nbrs_of_bytez == 0:  # Start processing a new UTF-8 character
            for i in binary_rep:
                if i == '0':
                    break
                nbrs_of_bytez += 1

            if nbrs_of_bytez == 0:  # Invalid start of a character
                continue

            # Invalid number of bytes for a character
            if nbrs_of_bytez == 1 or nbrs_of_bytez > 4:
                return False
        else:
            # Check if the byte is a continuation byte
            if not binary_rep.startswith('10'):
                return False
        nbrs_of_bytez -= 1

    return nbrs_of_bytez == 0  # Check if all characters have been completed
