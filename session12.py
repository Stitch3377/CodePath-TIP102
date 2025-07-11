"""
Session 12: Unit 6
Breakout Problem Set - Standard Version 1
"""


class Node:
    """Node class"""

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_circular(clues):
    """Problem 1"""
    if clues is None:
        return False

    current = clues

    while current.next:
        if current.next == clues:
            return True
        current = current.next
    return False
