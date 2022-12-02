#!/usr/bin/env python3
""" Module to transpose a matrix """


def np_transpose(matrix):
    """ Transposes matrix and returns a new array """

    new_array = matrix.copy()
    transposed_array = new_array.transpose()
    return transposed_array
