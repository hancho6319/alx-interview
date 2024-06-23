#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def print_stats():
    """Print the accumulated metrics"""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")


def handle_interrupt(signum, frame):
    """Handle keyboard interrupt (CTRL + C)"""
    print_stats()
    sys.exit(0)


# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line_count += 1

        # Split the line and validate the format
        parts = line.split()
        if len(parts) < 9:
            continue

        ip = parts[0]
        dash = parts[1]
        date_part1 = parts[2]
        date_part2 = parts[3]
        date_part3 = parts[4]
        method = parts[5]
        resource = parts[6]
        protocol = parts[7]
        status_code_str = parts[8]

        # Ensure there is a file size part
        if len(parts) > 9:
            file_size_str = parts[9]
        else:
            continue

        # Extract the status code and file size
        try:
            status_code = int(status_code_str)
            file_size = int(file_size_str)
        except ValueError:
            continue

        # Update metrics
        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    handle_interrupt(None, None)
finally:
    print_stats()
