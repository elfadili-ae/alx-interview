#!/usr/bin/python3
"""Parse logs"""
import sys
import re


def extract_data(log_line):
    pattern = re.compile(
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[([^\]]+)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    )
    match = pattern.match(log_line)

    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        return status_code, file_size
    else:
        return None, None


lines = []
codes = [200, 301, 400, 401, 403, 404, 405, 500]
codesCount = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}

output = []
total_size = 0
print_counter = 0
try:
    while True:
        line = input()
        print_counter += 1
        codo, saizu = extract_data(line)
        if codo is not None and saizu is not None:
            if codo in codesCount:
                codesCount[int(codo)] += 1
                total_size += saizu
        if print_counter == 10:
            print_counter = 0
            ln = "file size: {}".format(total_size)
            print(ln)
            for i in codes:
                if codesCount[i] != 0:
                    print("{}: {}".format(i, codesCount[i]))
except KeyboardInterrupt:
    ln = "file size: {}".format(total_size)
    for i in codes:
        if codesCount[i] != 0:
            ln += "\n{}: {}".format(i, codesCount[i])
    print(ln)
    sys.stdout.flush()
    raise
