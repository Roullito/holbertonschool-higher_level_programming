#!/usr/bin/python3
"""
Module for matrix_divided function.
Performs element-wise division on a matrix.
Rounds results to 2 decimal places.
"""

def matrix_divided(matrix, div):
    """
    Divide matrix values by div.
    Return a new matrix rounded to 2 decimals.
    """
    new_matrix = []
    row_len = len(matrix[0])
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                              for row in matrix):
        raise TypeError(
            "matrix must be a matrix "
                        "(list of lists) of integers/floats"
        )
    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
