#!/usr/bin/python3
'''Rotate a 2D matrix'''


def rotate_2d_matrix(matrix):
    '''rotates a 2D matrix by 90 degrees'''
    new_matrix = []
    length = len(matrix)

    if length == 1:
        return

    for i in range(length):
        child_list = []
        for j in reversed(range(length)):
            child_list.append(matrix[j][i])
        new_matrix.append(child_list)

    matrix[::] = new_matrix
