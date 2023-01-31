#!/usr/bin/python3
import copy

''' lockbox algorithm'''

def canUnlockAll(boxes):
    if len(boxes) == 0:
        return False
    hash = {}
    for index, box in enumerate(boxes):
        hash[index] = box

    keysafe = []

    for box in boxes:
        for num in box:
            keysafe.append(num)

    for key in hash.keys():
        if key != 0:
            if key not in keysafe:
                return False
            if key in boxes[key]:
                keysafe.remove(key)
                if key not in keysafe:
                    return False
    return True
