import random

def get_primes(n):
    """Returns a list of primes up to n."""
    primes = [2]
    for i in range(3, n+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


nums = [random.randint(1, 10000) for i in range(100)]
x = 100

print(get_primes(10000))

# #!/usr/bin/python3
# """0x0A. Prime Game"""


# def isWinner(x, nums):
#     """ a function that returns the winner"""
#     if len(nums) < x or x < 1 or len(nums) == 0:
#         return None

#     spread_nums = [[i for i in range(1, j+1)] for j in nums]
#     buffer = deep_copy_list(spread_nums)
#     round = 0
#     ben = 0
#     maria = 0
#     player = 0

#     for spread in spread_nums:
#         checker = 0
#         player = 0
#         for i in spread:
#             if i == checker:
#                 continue
#             elif is_prime(i):
#                 for j in spread:
#                     if j % i == 0 and j in buffer[round]:
#                         buffer[round].remove(j)
#                         checker = i
#                 player += 1
#         if buffer[round] == [1]:
#             if is_even(player):
#                 ben += 1
#             else:
#                 maria += 1
#         round += 1

#     if ben > maria:
#         return "Ben"
#     elif maria > ben:
#         return "Maria"
#     else:
#         return None


# def is_prime(n):
#     """
#     Returns True if the input number n is prime, False otherwise.
#     """
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# def deep_copy_list(original_list):
#     """makes a deep copy of list"""
#     copy_list = []
#     for item in original_list:
#         if isinstance(item, list):
#             item_copy = deep_copy_list(item)
#             copy_list.append(item_copy)
#         else:
#             copy_list.append(item)
#     return copy_list


# def is_even(number):
#     """ checks for even number"""
#     return number % 2 == 0
