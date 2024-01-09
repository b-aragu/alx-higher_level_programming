#!/usr/bin/python3

import sys
import signal


def print_statistics(total_size, status_counts):
    """Prints the computed statistics."""
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts):
        print("{}: {}".format(status_code, status_counts[status_code]))


def signal_handler(sig, frame):
    """Handles the SIGINT signal and prints statistics before exiting."""
    print_statistics(total_size, status_counts)
    sys.exit(0)


total_size = 0
status_counts = {}

signal.signal(signal.SIGINT, signal_handler)

try:
    for i, line in enumerate(sys.stdin, start=1):
        data = line.split()
        if len(data) >= 8:
            status_code = data[-2]
            file_size = int(data[-1])

            total_size += file_size
            codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

            if status_code in codes:
                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1

        if i % 10 == 0:
            print_statistics(total_size, status_counts)

except KeyboardInterrupt:
    print_statistics(total_size, status_counts)
    sys.exit(0)
