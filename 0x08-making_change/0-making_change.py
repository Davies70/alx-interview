#!/usr/bin/python3
""" Change comes from within"""


# def makeChange(coins, total):
#     """Given a pile of coins of different values,
#           determine the fewest number of coins needed to \
#          meet a given amount total."""
#     if total <= 0:
#         return 0

#     dp = [float('inf')] * (total + 1)
#     dp[0] = 0

#     for coin in coins:
#         for i in range(coin, total + 1):
#             dp[i] = min(dp[i], dp[i - coin] + 1)

#     return dp[total] if dp[total] != float('inf') else -1

""" 0. Change comes from within """


# Given a pile of coins of different values,
# determine the fewest number of coins needed to
# meet a given amount total

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
