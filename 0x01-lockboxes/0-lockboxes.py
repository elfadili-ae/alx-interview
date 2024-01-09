#!/usr/bin/python3
"""Lockboxes problem."""


def canUnlockAll(boxes):
    """Unlock boxes."""
    def getKeys(box, keys):
        """Get keys from the box"""
        for key in box:
            keys[key] = 1

    keys = {}
    notOpened = []
    if len(boxes) == 0 or len(boxes) == 1:
        return True

    for i in range(1, len(boxes)):
        getKeys(boxes[i - 1], keys)
        if i not in keys:
            if i not in keys:
                notOpened.append(i)

    for i in notOpened:
        if i not in keys:
            return False

    return True
