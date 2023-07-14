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
    exactly n H characters in the files
    """
    minop = 0

    for i in range(2, n + 1):
        while(n % i == 0):
            minop += i
            n /= i
    return minop
