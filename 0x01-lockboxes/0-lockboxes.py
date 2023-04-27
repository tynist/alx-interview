#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes
"""


def canUnlockAll(box):
    """
    Determine if all the boxes can be opened.

    :param box: A list of lists representing boxes with keys to other boxes.
    :return: True if all boxes can be opened, otherwise False.
    """
    # Check if box is a non-empty list
    if not box or type(box) is not list:
        return False

    # Initialize list of unlocked boxes with the first box
    unlocked_boxes = [0]

    # Loop through each unlocked box and its keys
    for current_box in unlocked_boxes:
        for key in box[current_box]:
            # Check if key has not been used to unlock a box yet and is a valid box index
            if key not in unlocked_boxes and key < len(box):
                # Add key to the list of unlocked boxes
                unlocked_boxes.append(key)

    # Check if all boxes have been unlocked
    if len(unlocked_boxes) == len(box):
        return True
    else:
        return False
