#!/usr/bin/python3
"""0x0A. Prime Game"""


def isWinner(x, nums):
    """ a function that returns the winner"""
    if len(nums) < x:
        return None

    nums = nums[:x]
    spread_nums = [[i for i in range(1, j+1)] for j in nums]
    buffer = deep_copy_list(spread_nums)
    round = 0
    ben = 0
    maria = 0
    player = 0

    for spread in spread_nums:
        checker = 0
        player = 0
        for i in spread:
            if i == checker:
                continue
            elif is_prime(i):
                for j in spread:
                    if j % i == 0:
                        buffer[round].remove(j)
                        checker = i
                player += 1
        if buffer[round] == [1]:
            if is_even(player):
                ben += 1
            else:
                maria += 1
        round += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None


def is_prime(n):
    """
    Returns True if the input number n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def deep_copy_list(original_list):
    copy_list = []
    for item in original_list:
        if isinstance(item, list):
            item_copy = deep_copy_list(item)
            copy_list.append(item_copy)
        else:
            copy_list.append(item)
    return copy_list


def is_even(number):
    return number % 2 == 0
