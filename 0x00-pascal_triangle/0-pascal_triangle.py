#!/usr/bin/python3

"""
function def pascal_triangle(n) returns a list of lists of integers \
     representing the Pascal’s triangle of n:
Returns an empty list if n <= 0
You can assume n will be always an integer
"""


def pascal_triangle(n):
    """ returns a list of lists of numbers"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    new_row = [1]
    result = pascal_triangle(n - 1)
    last_row = result[-1]
    for i in range(len(last_row) - 1):
        num = last_row[i] + last_row[i + 1]
        new_row.append(num)

    new_row.append(1)
    result.append(new_row)
    return result
