#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing the data set.

    Returns:
        True if data is a valid UTF-8 encoding, else return False.
    """

    # Check if each byte in the data set is in the range 0x00 to 0xFF.
    for byte in data:
        if byte < 0x00 or byte > 0xFF:
            return False

    # Checks if first byte of each character is in range 0xC2 to 0xF7
    for i in range(0, len(data), 2):
        if data[i] not in range(0xC2, 0xF8):
            return False

    # Checks if continuation bytes of each xter are in range 0x80 - 0xBF
    for i in range(1, len(data), 2):
        if data[i] not in range(0x80, 0xBF):
            return False

    return True
