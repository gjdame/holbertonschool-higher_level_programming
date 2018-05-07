#!/usr/bin/python3


def matrix_divided(matrix, div):
    """divides contents of matrix by div
    Args:
        matrix: matrix of elements
        div: divisor
    """

    message = 'matrix must be a matrix (list of lists) of integers/fl\
oats'
    if all(isinstance(row, list) for row in matrix) is False:
        raise TypeError(message)
    if all(isinstance(e, (int, float)) for r in matrix for e in r) is False:
        raise TypeError(message)

    x = len(matrix[0])
    if x == 0:
        raise TypeError(message)
    for row in matrix:
        if len(row) is not x:
            raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')
    else:
        new_matrix = [[round(elem / div, 2) for elem in row]
                      for row in matrix]

    return(new_matrix)
