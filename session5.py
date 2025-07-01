# Problem 1
# Inputs: String with (), [], {}
# Outputs: boolean, true if valid/balance, false otherwise
# Constraints: only (), [], {}
# Edge cases: no brackets, empty string
def is_valid_post_format(posts):
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


print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}"))
print(is_valid_post_format("(]"))


def is_balanced_parentheses(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}"))
# print(is_valid_post_format("(]"))


# Problem 2
# Inputs: Queue of comments (list of strings)
# Outputs:
# Constraints:
# Edge cases:
def reverse_comments_queue(comments):
    stack = []
    for i in range(len(comments)):
        stack.append(comments.pop())
    return stack


# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


# Problem 3
def is_symmetrical_title(title):
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


# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media"))
