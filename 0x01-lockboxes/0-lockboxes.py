'''
lockboxes module
'''
#!/usr/bin/python3
import copy

''' lockbox algorithm'''

def canUnlockAll(boxes):
    ''' check if all boxes can be unlocked'''
    if len(boxes) == 0:
        return False
    hash = {}
    for index, box in enumerate(boxes):
        hash[index] = box

    keysafe = []
    i = 0

    for box in boxes:
        for num in box:
            keysafe.append(num)

    for key in hash.keys():
        if key != 0:
            if key not in keysafe:
                return False
            if key in boxes[key]:
                occurence = boxes[key].count(key)
                while i < occurence:
                    keysafe.remove(key)
                    i += 1
                if key not in keysafe:
                    return False
    return True
