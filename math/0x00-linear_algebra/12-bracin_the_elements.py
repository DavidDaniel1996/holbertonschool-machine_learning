#!/usr/bin/env python3
""" Module to add, substract, multiply and divide numpy array """


def np_elementwise(mat1, mat2):
    """ Perform module operations, returning a tuple with the results """

    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)

    # sum_matrix = []
    # sub_matrix = []
    # mult_matrix = []
    # div_matrix = []

    # for i in range(len(mat1)):
    #     sum_array = []
    #     sub_array = []
    #     mult_array = []
    #     div_array = []
    #     for j in range(len(mat1[i])):
    #         sum_array.append(mat1[i][j] + mat2[i][j])
    #         sub_array.append(mat1[i][j] - mat2[i][j])
    #         mult_array.append(mat1[i][j] * mat2[i][j])
    #         div_array.append(mat1[i][j] / mat2[i][j])
    #     sum_matrix.append(sum_array)
    #     sub_matrix.append(sub_array)
    #     mult_matrix.append(mult_array)
    #     div_matrix.append(div_array)

    # return(sum_matrix, sub_matrix, mult_matrix, div_matrix)
