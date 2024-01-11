#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics
"""


import signal
import sys

def signal_handler(signal, frame):
    print_metrics()
    sys.exit(0)

def print_metrics():
    global total_file_size
    global status_code_counts

    print("Total file size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts.get(status_code, 0)
        if count > 0:
            print(f"{status_code}: {count}")

if __name__ == "__main__":
    total_file_size = 0
    status_code_counts = {}

    line_count = 0

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            
            if len(data) >= 10:
                status_code = data[-2]
                file_size = int(data[-1])
                
                total_file_size += file_size
                
                status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1
                
                if line_count % 10 == 0:
                    print_metrics()

    except KeyboardInterrupt:
        print_metrics()
