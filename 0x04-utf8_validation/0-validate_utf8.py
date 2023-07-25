#!/usr/bin/python3
"""a method that determines if a given data set is a valid UTF-8 encoding"""


def validUTF8(data):
    """ method that determines if a given data set is a valid UTF-8 encoding"""
    count = 0
    for num in data:
        if count == 0:
            if (num >> 7) != 0:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            count -= 1
    return count == 0
