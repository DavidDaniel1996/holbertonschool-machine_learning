#!/usr/bin/env python3
""" Module to add two arrays together, element wise """


def add_arrays(arr1, arr2):
    """ Adds two arrays together """

    if len(arr1) != len(arr2):
        return None

    new_list = []

    for i in range(len(arr1)):
        sum_total = arr1[i] + arr2[i]
        new_list.append(sum_total)

    return new_list
