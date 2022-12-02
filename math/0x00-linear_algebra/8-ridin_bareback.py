#!/usr/bin/env python3
""" Module multiplies 2 matrices """


def mat_mul(mat1, mat2):
    """ Multiplies 2d matrices, returning new matrix """

    new_matrix = []

    if len(mat1[0]) != len(mat2):
        return None

    for i in range(len(mat1)):
        new_array = []
        for j in range(len(mat2[0])):
            sum_array = []
            for k in range(len(mat2)):
                element_mult = mat1[i][k] * mat2[k][j]
                sum_array.append(element_mult)
            result = 0
            for n in range(len(sum_array)):
                result = result + sum_array[n]
            new_array.append(result)
        new_matrix.append(new_array)

    return new_matrix
