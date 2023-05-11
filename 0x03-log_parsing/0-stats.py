#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys


def print_status(status_counts, total_fil_size):
    "““Prints the statistics in the specified format. 

    Args:
        status_counts (dict): A dictionary containing the status codes
        and their respective counts.
        total_fil_size (int): The total file size.

    Prints:
        The file size and the number of lines for each status code.
    """
    print("Total file size:", total_fil_size)
    for code in sorted(status_counts.keys()):
        if status_counts[code] != 0:
            print("{}: {}".format(code, status_counts[code]))


status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                 '404': 0, '405': 0, '500': 0}

total_fil_size = 0
line_count = 0

try:
    for line in sys.stdin:
        if line_count != 0 and line_count % 10 == 0:
            # Print statistics every 10 lines
            print_status(status_counts, total_fil_size)

        elements = line.split(" ")
        line_count += 1

        try:
            # Gets file size from the last element of the line
            fil_size = int(elements[-1])
            total_fil_size += fil_size  # Increment total file size
        except IndexError:
            pass

        try:
            status_code = elements[-2]
            # check if the status code is present in the dictionary
            if status_code in status_counts:
                # increment the count for the corresponding status code
                status_counts[status_code] += 1
        except IndexError:
            pass

    # Print final statistics
    print_status(status_counts, total_fil_size)

except KeyboardInterrupt:
    # If interrupted, print the current statistics and raise the exception
    print_status(status_counts, total_fil_size)
    raise
