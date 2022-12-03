#!/usr/bin/env python3
""" Module to concatenate two 2d matrices """

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """ Concatenate two 2d numpy arrays, returning a new one """

    new_mat1 = mat1.copy()
    new_mat2 = mat2.copy()

    return (np.concatenate((mat1, mat2), axis=axis))
