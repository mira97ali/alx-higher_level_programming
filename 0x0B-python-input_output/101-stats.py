#!/usr/bin/python3
"""Log parsing"""
import sys


def print_metrics(total_size, status_codes):
    """Print metrics based on current statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {}

    try:
        for idx, line in enumerate(sys.stdin, 1):
            parts = line.split()
            if len(parts) > 7:
                total_size += int(parts[-1])
                status_code = int(parts[-2])

                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

            if idx % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (CTRL + C)
        print_metrics(total_size, status_codes)
        sys.exit(0)
