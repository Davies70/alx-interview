#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [0], [0], [0], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 8], [2], [0, 4, 1], [5, 99, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3, 3, 3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
