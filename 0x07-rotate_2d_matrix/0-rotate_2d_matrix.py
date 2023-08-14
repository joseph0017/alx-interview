#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    # reverse
    left = 0
    right = len(matrix) - 1
    while left < right:
        matrix[left], matrix[right] = matrix[right], matrix[left]
        left += 1
        right -= 1
    # transpositon os matrix
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
