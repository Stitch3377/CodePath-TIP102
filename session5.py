"""
Session 5: Unit 3
Breakout Problem Set - Standard Version 2
"""

from collections import deque


def is_valid_post_format(posts):
    """Problem 1"""
    stack = []
    for char in posts:
        if len(stack) == 0:
            stack.append(char)
        else:
            if char == "}" and stack.pop() != "{":
                return False
            elif char == "]" and stack.pop() != "[":
                return False
            elif char == ")" and stack.pop() != "(":
                return False
    return True


print("Problem 1:")
print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}"))
print(is_valid_post_format("(]"))
print()


def reverse_comments_queue(comments):
    """Problem 2"""
    stack = []
    for i in range(len(comments)):
        stack.append(comments.pop())
    return stack


print("Problem 2:")
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
print()


def is_symmetrical_title(title):
    """Problem 3"""
    stack = []
    pointer1 = 0
    pointer2 = len(title) - 1
    while pointer1 != pointer2:
        while not title[pointer1].isalpha():
            pointer1 += 1
        while not title[pointer2].isalpha():
            pointer2 -= 1
        stack.append(title[pointer1].upper())
        if title[pointer2].upper() != stack.pop():
            return False
        pointer1 += 1
        pointer2 -= 1
    return True


print("Problem 3:")
print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))
print()


def engagement_boost(engagements):
    """Problem 4"""
    length = len(engagements)
    result = [0] * length
    left = 0
    right = length - 1
    pos = length - 1

    while left <= right:
        abs_left = abs(engagements[left])
        abs_right = abs(engagements[right])

        if abs_left > abs_right:
            result[pos] = engagements[left] ** 2
            left += 1
        else:
            result[pos] = engagements[right] ** 2
            right -= 1
        pos -= 1
    return result


print("Problem 4:")
print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
print()


def clean_post(post):
    """Problem 5"""
    stack = []

    for letter in post:
        if not stack:
            stack.append(letter)
        else:
            prev = stack[-1]
            if (prev.lower() == letter.lower()) and (
                prev.isupper() and letter.islower()
            ):
                stack.pop()
            elif (prev.lower() == letter.lower()) and (
                prev.islower() and letter.isupper()
            ):
                stack.pop()
            else:
                stack.append(letter)

    return "".join(stack)


print("Problem 5:")
print(clean_post("poOost"))
print(clean_post("abBAcC"))
print(clean_post("s"))
print()


def edit_post(post):
    """Problem 6"""
    result = ""

    for word in post.split():
        queue = deque()
        for letter in word:
            queue.appendleft(letter)
        result += " " + "".join(queue)
    return result[1:]


print("Problem 6:")
print(edit_post("Boost your engagement with these tips"))
print(edit_post("Check out my latest vlog"))
print()


def post_compare(draft1, draft2):
    """Problem 7"""
    stack1 = []
    stack2 = []

    if len(draft1) != len(draft2):
        return False

    for char in draft1:
        if stack1:
            if char == "#":
                stack1.pop()
            else:
                stack1.append(char)
        else:
            pass

    for char in draft2:
        if stack2:
            if char == "#":
                stack2.pop()
            else:
                stack2.append(char)
        else:
            pass

    return "".join(stack1) == "".join(stack2)


print("Problem 7:")
print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#"))
print(post_compare("a#c", "b"))
print()
