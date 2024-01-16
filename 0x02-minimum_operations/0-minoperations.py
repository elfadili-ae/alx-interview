#!/usr/bin/python3
"""Min operations."""


def minOperations(n):
    """Min operations to get to Hxn."""
    res = 0
    printed = 1
    cp = 0
    paste = False
    for i in range(0, n):
        if printed == n:
            break
        res += 1
        if not paste:
            cp = printed
            paste = True
        else:
            printed += cp
            if n % printed == 0:
                paste = False
            else:
                paste = True
    return res
