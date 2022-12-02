#!/usr/bin/env python3

def add_matrices2D(mat1, mat2):

    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    new_matrix = []

    for i in range(len(mat1)):
        element_sum = []
        for j in range(len(mat1[0])):
            element_sum.append(mat1[i][j] + mat2[i][j])
        new_matrix.append(element_sum)

    return new_matrix
