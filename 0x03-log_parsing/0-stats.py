#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys


def print_status(status_dict, file_size):
    """Print the metrics"""
    print("Total file size: {}".format(file_size))
    for code in sorted(status_dict.keys()):
        if status_dict[code] != 0:
            print("HTTP {} count: {}".format(code, status_dict[code]))


status_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
               '404': 0, '405': 0, '500': 0}

total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        if line_count != 0 and line_count % 10 == 0:
            print_status(status_dict, total_size)

        elements = line.split(" ")
        line_count += 1

        try:
            size = int(elements[-1])
            total_size += size
        except:
            pass

        try:
            status_code = elements[-2]
            if status_code in status_dict.keys():
                status_dict[status_code] += 1
        except:
            pass

    print_status(status_dict, total_size)

except KeyboardInterrupt:
    print_status(status_dict, total_size)
    raise
