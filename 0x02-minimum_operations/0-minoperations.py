#!/usr/bin/python3
'''
Minimun operation
'''


def minOperations(n):
    '''takes number of characters as parameter
    returns the minimum number of operations'''
    if n <= 1:
        return 0

    # Find the largest factor of n that is not n itself
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return minOperations(i) + (n // i)

    # If n is prime, it can't be split into factors
    return n
