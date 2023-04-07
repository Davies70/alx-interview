import random

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print('.....')
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

# Test case 1
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))

# Test case 2
x = 2
nums = [2, 3]
print(isWinner(x, nums))

# Test case 3
x = 4
nums = [10, 7, 5, 3]
print(isWinner(x, nums))

# Test case 4
x = 3
nums = [1, 2, 3]
print(isWinner(x, nums))

# Test case 5
x = 1
nums = [5]
print(isWinner(x, nums))

#test case6

nums = [random.randint(1, 10000) for i in range(100)]
x = 100

print(isWinner(x, nums))

#test case7

print('.......')

nums = [random.randint(1, 10000) for i in range(10000)]
x = 10000

print(isWinner(x, nums))
