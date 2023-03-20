#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]


    rotate_2d_matrix(matrix)
    print(matrix)
    # Test case 1
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_2d_matrix(matrix1)
    print(matrix1)
    # Expected output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # Test case 2
    matrix2 = [[1, 2], [3, 4]]
    rotate_2d_matrix(matrix2)
    print(matrix2)
    # Expected output: [[3, 1], [4, 2]]

    # Test case 3
    matrix3 = [[1]]
    rotate_2d_matrix(matrix3)
    print(matrix3)
    # Expected output: [[1]]

    # Test case 4
    matrix4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotate_2d_matrix(matrix4)
    print(matrix4)
    # Expected output: [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

