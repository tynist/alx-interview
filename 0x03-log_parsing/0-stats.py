#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys


def print_status(dict, size):
    """
    Args:
        status_dict (dict): Dictionary contains the status codes and
        their respective counts.
        file_size (int): The total file size.

    Prints:
        The file size and the number of lines for each status code
    """
    print("File size: {}".format(size))
    for key in sorted(dict.keys()):
        if dict[key] != 0:
            print("{}: {}".format(key, dict[key]))


status_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
               '404': 0, '405': 0, '500': 0}

file_size = 0  # Total file size counter
line_count = 0  # Number of lines read from input

try:
    for line in sys.stdin:
        if line_count != 0 and line_count % 10 == 0:
            # Print metrics every 10 lines
            print_status(status_dict, file_size)

        elem = line.split(" ")  # Split the line by space
        line_count += 1

        try:
            # Get file size from the last element
            file_size += int(elem[-1])
        except:
            pass

        try:
            # Get HTTP status code from the second-to-last element
            if elem[-2] in status_dict.keys():
                status_dict[elem[-2]] += 1
        except:
            pass
    print_status(status_dict, file_size)  # print final metrics

except KeyboardInterrupt:   # Handle KeyboardInterrupt exception
    print_status(status_dict, file_size)
    raise
