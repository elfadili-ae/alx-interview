#!/usr/bin/python3
"""Parse logs"""
import sys


def printer(codes, codesCount, total_size):
    """Print output"""
    print("file size: {}".format(total_size))
    for i in codes:
        if codesCount[i] != 0:
            print("{}: {}".format(i, codesCount[i]))


if __name__ == "__main__":

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

    total_size = 0
    print_counter = 0
    try:
        for line in sys.stdin:
            if print_counter != 0 and print_counter % 10 == 0:
                printer(codes, codesCount, total_size)

            vals = line.split()
            print_counter += 1

            try:
                total_size += int(vals[-1])
            except Exception:
                pass

            try:
                if int(vals[-2]) in codesCount:
                    codesCount[int(vals[-2])] += 1
            except Exception:
                pass
        printer(codes, codesCount, total_size)

    except KeyboardInterrupt:
        printer(codes, codesCount, total_size)
        raise
