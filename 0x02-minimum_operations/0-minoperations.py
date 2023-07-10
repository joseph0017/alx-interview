#!/usr/bin/python3
"""
Given a number n, write a method that calculates the
fewest number of operations needed to result in
exactly n H characters in the file
"""


def minOperations(n):
    """
    Given a number n, write a method that calculates the
    fewest number of operations needed to result in
    exactly n H characters in the file
    """
    ca = 0
    p = 1
    if n <= 1:
        return 0
    for i in range(0, n - 2):
        if i % 2 == 0:
            ca = p + i + 5
            summ = ca // 2
    return summ
