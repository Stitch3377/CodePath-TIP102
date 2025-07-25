"""
Session 16: Unit 8
Breakout Problem Set - Standard Version 1
"""

from collections import deque


# Tree Node class
class TreeNode:
    "Tree node class"

    def __init__(self, value, key=None, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right


def build_tree(values):
    """Build tree"""
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_value, left_key)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_value, right_key)
            queue.append(node.right)
        index += 1
    return root


def print_tree(root):
    """Print tree"""
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


def count_odd_splits(root):
    """Problem 1"""

    if root is None:
        return 0

    if root.val % 2 == 1:
        return count_odd_splits(root.left) + count_odd_splits(root.right) + 1
    else:
        return count_odd_splits(root.left) + count_odd_splits(root.right)


print("Problem 1:")
r"""
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12
"""
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))
print()


def find_flower(inventory, name):
    """Problem 2"""

    if inventory is None:
        return False

    if inventory.val is name:
        return True

    return find_flower(inventory.left, name) or find_flower(inventory.right, name)


print("Problem 2:")
r"""
          Rose
         /    \
      Lilac  Tulip
      /  \       \
   Daisy Lily   Violet
"""

values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))
print(find_flower(garden, "Sunflower"))
print()


def non_bst_find_flower(root, name):
    """Problem 3"""
    if root is None:
        return False

    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)


print("Problem 3:")
r"""
         Daisy
        /    \
      Lily   Tulip
     /  \       \
  Rose  Violet  Lilac
"""

values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(non_bst_find_flower(garden, "Lilac"))
print(non_bst_find_flower(garden, "Sunflower"))
print()


def add_plant(collection, name):
    """Problem 4"""
    if not collection:
        return TreeNode(name)

    if name > collection.val:
        collection.right = add_plant(collection.right, name)
    elif name < collection.val:
        collection.left = add_plant(collection.left, name)
    return collection


print("Problem 4:")
r"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))
print()


def sort_plants(collection):
    """Problem 5"""

    if collection is None:
        return []

    return (
        sort_plants(collection.left)
        + [(collection.key, collection.val)]
        + sort_plants(collection.right)
    )


print("Problem 5:")
r"""
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
"""

# Using build_tree() function at the top of page
values = [
    (3, "Monstera"),
    (1, "Pothos"),
    (5, "Witchcraft Orchid"),
    None,
    (2, "Spider Plant"),
    (4, "Hoya Motoskei"),
]
collection = build_tree(values)

print(sort_plants(collection))
print()


def pick_plant(root, budget):
    """Problem 6"""

    largest = None

    current = root
    while current:
        if current.key < budget:
            largest = current
            current = current.right
        else:
            current = current.left

    if largest is None:
        return largest
    else:
        return largest.val


print("Problem 6:")
r"""
               (50, "Fiddle Leaf Fig")
             /                       \
    (25, "Monstera")           (70, "Snake Plant")
       /        \                   /         \
(15, "Aloe")  (40, "Pothos")  (60, "Fern")  (80, "ZZ Plant")
"""

values = [
    (50, "Fiddle Leaf Fig"),
    (25, "Monstera"),
    (70, "Snake Plant"),
    (15, "Aloe"),
    (40, "Pothos"),
    (60, "Fern"),
    (80, "ZZ Plant"),
]
inventory = build_tree(values)

print(pick_plant(inventory, 50))
print(pick_plant(inventory, 25))
print(pick_plant(inventory, 15))
print()


def remove_plant(collection, name):
    """Problem 7"""
    if not collection:
        return None

    # Recursive search
    if name < collection.val:
        collection.left = remove_plant(collection.left, name)
    elif name > collection.val:
        collection.right = remove_plant(collection.right, name)
    else:
        # Node to delete found
        # Case 1: No children
        if not collection.left and not collection.right:
            return None
        # Case 2: One child
        elif not collection.left:
            return collection.right
        elif not collection.right:
            return collection.left
        # Case 3: Two children
        else:
            # Find inorder predecessor (rightmost of left subtree)
            pred = collection.left
            while pred.right:
                pred = pred.right
            # Replace root's value with predecessor's value
            collection.val = pred.val
            # Remove predecessor from left subtree
            collection.left = remove_plant(collection.left, pred.val)

    return collection


print("Problem 7:")
r"""
              Money Tree
             /         \
           Hoya        Pilea
              \        /   \
             Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))
print()
