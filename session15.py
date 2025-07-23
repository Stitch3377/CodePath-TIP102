"""
Session 15: Unit 8
Breakout Problem Set - Standard Version 1
"""

from collections import deque


class TreeNode:
    """Tree Node Class"""

    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def print_tree(root):
    "Print tree function"
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


print("Problem 1:")
root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh")
root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")

root.right = TreeNode("Granny Smith")
root.right.left = TreeNode("Crab")
root.right.right = TreeNode("Gala")

print_tree(root)
print()


def calculate_yield(root):
    """Problem 2"""
    if not root or not root.left or not root.right:
        raise ValueError("Tree must have exactly 3 nodes.")

    left_val = root.left.val
    right_val = root.right.val

    if root.val == "+":
        return left_val + right_val
    elif root.val == "-":
        return left_val - right_val
    elif root.val == "*":
        return left_val * right_val
    elif root.val == "/":
        return left_val / right_val
    else:
        raise ValueError(f"Unknown operator: {root.val}")


print("Problem 2:")
"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

print(calculate_yield(apple_tree))
print()


def right_vine_iterative(root):
    """Problem 3"""
    vines = []

    if root:
        vines.append(root.val)

    current = root
    while current.right:
        vines.append(current.right.val)
        current = current.right

    return vines


print("Problem 3:")
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine_iterative(ivy1))
print(right_vine_iterative(ivy2))
print()


def right_vine_recursive(root):
    """Problem 4"""

    if root is None:
        return []

    return [root.val] + right_vine_recursive(root.right)


print("Problem 4:")
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine_recursive(ivy1))
print(right_vine_recursive(ivy2))
print()


def count_leaves(root):
    """Problem 5"""
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return count_leaves(root.left) + count_leaves(root.right)


print("Problem 5:")
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


print(count_leaves(oak1))
print(count_leaves(oak2))
print()


def survey_tree(root):
    """Problem 6"""
    if root is None:
        return []

    return survey_tree(root.left) + survey_tree(root.right) + [root.val]


print("Problem 6:")
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)

print(survey_tree(magnolia))
print()
