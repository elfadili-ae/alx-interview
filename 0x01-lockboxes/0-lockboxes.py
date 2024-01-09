#!/usr/bin/python3
"""Lockboxes problem."""


def canUnlockAll(boxes):
    """Unlock boxes."""
    def getKeys(box, keys):
        """Get keys from the box"""
        for key in box:
            keys[key] = 1

    keys = {0: 1}
    notOpened = []
    if len(boxes) == 0 or len(boxes) == 1:
        return True

    for i in range(0, len(boxes)):
        if i in keys:
            getKeys(boxes[i], keys)
        else:
            notOpened.append(i)

    for i in notOpened:
        if i in keys:
            getKeys(boxes[i], keys)
        else:
            return False

    return True
