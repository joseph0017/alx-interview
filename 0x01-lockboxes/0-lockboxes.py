#!/usr/bin/python3
"""function that unlocks all boxes if keys match"""


def canUnlockAll(boxes):
    """function to unlock boxes"""
    open_box = [0]
    for i in open_box:
        for j in boxes[i]:
            if j not in open_box:
                open_box.append(j)
    return len(open_box) == len(boxes)
