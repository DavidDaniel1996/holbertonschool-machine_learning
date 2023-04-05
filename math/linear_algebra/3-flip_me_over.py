#!/usr/bin/env python3
""" Module to find the transpose of a 2d matrix """


def matrix_transpose(matrix):
    """ Returns transpose of 2d matrix """

    new_matrix = []
    for i in range(len(matrix[0])):
        array = []
        for j in range(len(matrix)):
            array.append(matrix[j][i])
        new_matrix.append(array)

    return new_matrix
