#!/usr/bin/env python3
""" Module to add, substract, multiply and divide numpy array """


def np_elementwise(mat1, mat2):
    """ Perform module operations, returning a tuple with the results """

    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
