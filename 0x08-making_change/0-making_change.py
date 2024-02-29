#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """making change with the lowset number of coins"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num_coins = 0
    remaining_total = total

    for coin in coins:
        while remaining_total >= coin:
            remaining_total -= coin
            num_coins += 1

    if remaining_total == 0:
        return num_coins
    else:
        return -1
