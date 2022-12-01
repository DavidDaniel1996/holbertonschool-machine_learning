#!/usr/bin/python3

import numpy as np


def matrix_shape(matrix):
    np_array = np.array(matrix)
    return(list(np_array.shape))
