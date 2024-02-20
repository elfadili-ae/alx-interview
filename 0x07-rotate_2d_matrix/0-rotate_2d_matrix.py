#!/usr/bin/python3
"""Rotate 2d matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2d matrix nxn 90deg clockwise"""
    n = len(matrix)
    swaped = {}

    for i in range(0, n):
        for j in range(0, n):
            key1 = str(i) + "," + str(j)
            key2 = str(j) + "," + str(i)
            if key1 not in swaped and key2 not in swaped:
                swaped[str(i) + "," + str(j)] = 1
                swaped[str(j) + "," + str(i)] = 1
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

    for i in range(0, n):
        for j in range(0, n//2):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[i][n - 1 - j]
            matrix[i][n - 1 - j] = tmp
