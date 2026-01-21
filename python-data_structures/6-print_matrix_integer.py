#!/usr/bin/python3
"""
Write a function that prints a matrix of integers.
"""

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(col) for col in row))
