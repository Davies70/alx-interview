#!/usr/bin/python3
"""0x0A. Prime Game"""


def isWinner(x, nums):
    ''' winner of prime game'''
    if len(nums) < x or x < 1 or len(nums) == 0:
        return None

    max_num = max(nums)
    primes = get_primes(max_num)

    spread_nums = [[i for i in range(1, j+1)] for j in nums]
    buffer = [set(s) for s in spread_nums]
    ben = 0
    maria = 0
    player = 0

    for i in range(len(spread_nums)):
        player = 0
        for prime in primes:
            if prime > spread_nums[i][-1]:
                break
            for j in spread_nums[i]:
                if j % prime == 0 and j in buffer[i]:
                    buffer[i].remove(j)
                    player += 1
        if len(buffer[i]) == 1 and 1 in buffer[i]:
            if player % 2 == 0:
                ben += 1
            else:
                maria += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None


def get_primes(n):
    """Returns a set of primes up to n."""
    primes = set([2])
    for i in range(3, n+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(i)
    return primes
