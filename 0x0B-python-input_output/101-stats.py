#!/usr/bin/python3
"""Log parsing"""
import sys


def print_metrics(total_size, status_codes):
    """Print metrics based on current statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))
