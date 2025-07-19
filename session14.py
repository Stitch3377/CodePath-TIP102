"""
Session 14: Unit 7
Breakout Problem Set - Standard Version 1
"""


def find_cruise_length(cruise_lengths, vacation_length):
    """Problem 1"""
    left, right = 0, len(cruise_lengths) - 1

    while left <= right:
        mid = (left + right) // 2
        if cruise_lengths[mid] == vacation_length:
            return True
        if cruise_lengths[mid] < vacation_length:
            left = mid + 1
        else:
            right = mid - 1
    return False


print("Problem 1:")
print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))
print()


def find_cabin_index(cabins, preferred_deck):
    """Problem 2"""
    return binary_search(cabins, preferred_deck, 0, len(cabins) - 1)


def binary_search(nums, target, left, right):
    """Problem 2"""
    if left > right:
        return left

    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search(nums, target, mid + 1, right)
    else:
        return binary_search(nums, target, left, mid - 1)


print("Problem 2:")
print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))
print()


def count_checked_in_passengers(rooms):
    """Problem 3"""


print("Problem 3:")
rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1))
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))
print()
