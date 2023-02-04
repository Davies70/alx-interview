#!/usr/bin/python3

'''
lockboxes module
'''


def canUnlockAll(boxes):
    ''' check if all boxes can be unlocked'''
    if len(boxes) == 0:
        return False
    keysafe = []

    for keys in boxes[0]:
        keysafe.append(keys)


    for index, value in enumerate(boxes):
        for index, value in enumerate(boxes):
            if index in keysafe and index != 0:
                keysafe = keysafe + value

    for i in range(1, len(boxes)):
        if i not in keysafe:
            return False

    return True
