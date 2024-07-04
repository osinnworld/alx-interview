#!/usr/bin/python3
"""
Module for lockboxes problem.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    # Initialize a set to keep track of visited boxes
    visited = set()

    # Initialize a queue with the first box
    queue = [0]

    # Mark the first box as visited
    visited.add(0)

    # While there are boxes in the queue
    while queue:
        current_box = queue.pop(0)

        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and that box has not been visited
            if key < len(boxes) and key not in visited:
                # Mark the box as visited and add it to the queue
                visited.add(key)
                queue.append(key)

    # If all boxes have been visited, return True
    return len(visited) == len(boxes)
