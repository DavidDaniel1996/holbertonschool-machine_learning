#!/usr/bin/env python3
""" Module concatenates two 2d matrices """


def cat_matrices2D(mat1, mat2, axis=0):
    """ Concatenates 2d matrices along specified axis """

    try:
        new_matrix = []

        for i in range(len(mat1)):
            new_row = []
            for j in range(len(mat1[i])):
                new_row.append(mat1[i][j])
            new_matrix.append(new_row)

        if axis == 0:
            for i in range(len(mat2)):
                new_matrix.append(mat2[i][:])

            return new_matrix

        elif axis == 1:
            for i in range(len(mat2)):
                for j in range(len(mat2[i])):
                    new_matrix[i].append(mat2[i][j])

            return new_matrix

        else:
            return None
    except Exception:
        return None
