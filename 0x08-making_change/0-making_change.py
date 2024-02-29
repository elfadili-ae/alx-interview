#!/usr/bin/python3
"""Making change"""

def makeChange(coins, total):
    """make change"""
    if total <= 0:
        return 0
    
    coins = sorted(coins)
    result = 0
    s = len(coins)
    for i in range(s - 1, -1, -1):
        if total % coins[s - 1 - i] != 0:
            for j in range(i - 1, -1, -1):
                if total % coins[j] == 0:
                    i = j - 1
                    result += 1
                    return result
        else:
            val = total // coins[i]
            total = total - (coins[i] * val)
            result += val


    if total == 0:
        return result
    return -1