#!/usr/bin/python3

def square_matrix_simple(matrix=[]):


    new_matrix = [[num * num for num in row] for row in matrix]
    return(new_matrix)
