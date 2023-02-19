#!/usr/bin/python3
'''reads stdin line by line and computes metrics'''
import sys

# Initialize variables
total_file_size = 0
status_code_counts = {}

try:
    # Read from stdin line by line
    for i, line in enumerate(sys.stdin, 1):
        # Parse the line
        parts = line.split()
        if len(parts) != 7:
            # Skip the line if the format is incorrect
            continue
        ip_address, _, _, path, status_code, file_size, _ = parts
        if path != '/projects/260':
            # Skip the line if the path is not '/projects/260'
            continue
        try:
            file_size = int(file_size)
            status_code = int(status_code)
        except ValueError:
            # Skip the line if the file size or status code is not an integer
            continue

        # Update the metrics
        total_file_size += file_size
        status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

        # Print the metrics every 10 lines
        if i % 10 == 0:
            print(f"Total file size: {total_file_size}")
            for status_code in sorted(status_code_counts.keys()):
                print(f"{status_code}: {status_code_counts[status_code]}")
            print()
except KeyboardInterrupt:
    # Print the final metrics on keyboard interruption
    print(f"\nTotal file size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        print(f"{status_code}: {status_code_counts[status_code]}")
