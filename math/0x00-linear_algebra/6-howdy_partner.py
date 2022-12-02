#!/usr/bin/env python3
""" Module to concatenate two arrays """


def cat_arrays(arr1, arr2):
    """ Returns new array of two concatenated arrays """

    new_array = []

    for i in range(len(arr1)):
        new_array.append(arr1[i])

    for j in range(len(arr2)):
        new_array.append(arr2[j])

    return new_array
