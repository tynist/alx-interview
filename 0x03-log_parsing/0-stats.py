#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys


def print_status(status_count_dict, file_size):
      """
    Args:
        status_count_dict (dict): dictionary contains the status codes and
        their respective counts.
        file_size (int): The total file size.7

    Prints:
        The file size and the number of lines for each status code
    """
    print("File size: {}".format(size))
    for key in sorted(dict.keys()):
        if dict[key] != 0:
            print("{}: {}".format(key, dict[key]))


status_count_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
               '404': 0, '405': 0, '500': 0}

file_size = 0
count = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_status(status_count_dict, file_size)

        el = line.split(" ")
        count += 1

        try:
            file_size += int(el[-1])
        except:
            pass

        try:
            if el[-2] in status_count_dict.keys():
                status_count_dict[el[-2]] += 1
        except:
            pass
    print_status(status_count_dict, file_size)


except KeyboardInterrupt:
    print_status(status_count_dict, file_size)
    raise
