#!/usr/bin/env python3
""" Module to calculate the shape of a matrix """


def matrix_shape(matrix):
    """ Calculates shape of a matrix """
    if matrix:
        try:
            shape = [len(matrix), len(matrix[0]), len(matrix[0][0])]
            return shape
        except TypeError:
            try:
                shape = [len(matrix), len(matrix[0])]
                return shape
            except TypeError:
                shape = [len(matrix)]
                return shape
