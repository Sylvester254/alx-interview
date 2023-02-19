#!/usr/bin/python3
import sys
"""_summary_
    script that reads stdin line by line and computes metrics
"""
total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1

        # Extracting information from log line
        try:
            parsed_line = line.split(" ")
            status_code = parsed_line[-2]
            file_size = int(parsed_line[-1])
            total_size += file_size
        except:
            continue

        # Updating status codes
        if status_code in status_codes:
            status_codes[status_code] += 1

        # Printing statistics
        if line_count == 10:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] != 0:
                    print("{}: {}".format(code, status_codes[code]))
            line_count = 0

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))
