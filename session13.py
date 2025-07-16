"""
Session 13: Unit 7
Breakout Problem Set - Standard Version 1
"""


def count_suits_iterative(suits):
    """Problem 1 Part 1"""
    count = 0
    for suit in suits:
        count += 1
    return count


def count_suits_recursive(suits):
    """Problem 1 Part 2"""
    if not suits:
        return 0
    else:
        return count_suits_recursive(suits[1::]) + 1


print("Problem 1:")
print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III", "Mark IV"]))
print()


def sum_stones(stones):
    """Problem 2"""
    if not stones:
        return 0
    else:
        return sum_stones(stones[1::]) + stones[0]


print("Problem 2:")
print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))
print()


def count_unique_suits_iterative(suits):
    "Problem 3 Part 1"
    count = 0
    for suit in set(suits):
        count += 1
    return count


def count_unique_suits_recursive(suits):
    "Problem 3 Part 2"

    # base case
    if not suits:
        return 0

    # recursive case 1
    if suits[0] in suits[1::]:
        return count_unique_suits_recursive(suits[1::])
    else:
        # recursive case 2
        return count_unique_suits_recursive(suits[1::]) + 1


print("Problem 3:")
print(count_unique_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_unique_suits_recursive(["Mark I", "Mark I", "Mark III"]))
print()


def fibonacci_growth(n):
    """Problem 4"""
    if n <= 1:
        return n

    return fibonacci_growth(n - 1) + fibonacci_growth(n - 2)


print("Problem 4:")
print(fibonacci_growth(5))
print(fibonacci_growth(8))
print()
