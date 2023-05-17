#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    number_of_bytes = 0  # number of bytes in the current UTF-8 char
    # goes into the numbers of the given set
    for numbers in data:
        # prints the 8least sig bits
        number_of_bin = format(numbers, '#010b')[-8:]
        if number_of_bytes == 0:  # start processing a new UTF-8 char

            # Get the number of 1s in the beginning of the string.
            for bit in number_of_bin:
                if bit == '0':
                    break
                number_of_bytes += 1

            if number_of_bytes == 0:  # 1 byte characters
                continue

            # A character in UTF-8 can be 1 to 4 bytes long
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:

            # Bytes which are a part of
            # a UTF-8 character must adhere
            # to the pattern `10xxxxxx`.
            if not number_of_bin.startswith('10'):
                return False

        # We reduce the number of bytes
        # to process by 1 after each integer.
        number_of_bytes -= 1

    return number_of_bytes == 0
