#!/usr/bin/python3
'''reads stdin line by line and computes metrics'''
import sys
import signal

stats = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_size = 0
line_count = 0

def print_stats():
    '''print stats'''
    print("File size: {}".format(total_size))
    for code in sorted(stats.keys()):
        if stats[code] > 0:
            print("{}: {}".format(code, stats[code]))

def handle_interrupt(sig, frame):
    '''interrupt handler'''
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

for line in sys.stdin:
    line_count += 1
    try:
        parts = line.strip().split()
        size = int(parts[-1])
        status_code = int(parts[-2])
        if status_code in stats:
            stats[status_code] += 1
        total_size += size
    except (IndexError, ValueError):
        continue

    if line_count % 10 == 0:
        print_stats()

print_stats()
