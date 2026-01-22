Here's your code formatted according to PEP 8 / pycodestyle:
python

#!/usr/bin/python3
"""Module for matrix division."""


def matrix_divided(matrix, div):
    """Divide matrix elements by div."""
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(err_msg)
    if len(matrix) == 0:
        raise TypeError(err_msg)
    if type(matrix[0]) is not list:
        raise TypeError(err_msg)
    if len(matrix[0]) == 0:
        raise TypeError(err_msg)

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(err_msg)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
