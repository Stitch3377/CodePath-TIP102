"""
Session 10: Unit 5
Breakout Problem Set - Standard Version 1
"""


class Villager:
    """Problem 1 Villager class"""

    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        """Problem 1"""
        my_friends = set()
        for friend in self.friends:
            my_friends.add(friend.name)

        their_friends = set()
        for friend in new_contact.friends:
            their_friends.add(friend.name)

        return list(my_friends & their_friends)


print("Problem 1:")
bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))
print()


class Node:
    """Node class"""

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

# Add code here to link the above nodes
kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

print("Problem 2:")
print_linked_list(kk_slider)
print()


def add_first(head, task):
    """Problem 3"""
    return Node(task, head)


print("Problem 3:")
task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

# Linked List: shake tree -> dig fossils -> catch bugs
print_linked_list(add_first(task_1, "check turnip prices"))
print()


def halve_list(head):
    """Problem 4"""
    current = head
    while current:
        current.value = current.value / 2
        current = current.next
    return head


print("Problem 4:")
node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(halve_list(node_one))
print()


def delete_tail(head):
    """Problem 5"""
    current = head

    while current.next.next:
        current = current.next

    current.next = None
    return head


print("Problem 5:")
butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))
print()


def find_min(head):
    """Problem 6"""
    minimum = head.value
    current = head
    while current:
        if minimum > current.value:
            minimum = current.value
        current = current.next
    return minimum


print("Problem 6:")
head1 = Node(5, Node(6, Node(7, Node(8))))
head2 = Node(8, Node(5, Node(6, Node(7))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_min(head1))

# Linked List: 8 -> 5 -> 6 -> 7
print(find_min(head2))
print()


def delete_item(head, item):
    """Problem 7"""
    current = head

    if head.value == item:
        return head.next

    while current.next:
        if current.next.value == item:
            if current.next.next is None:
                current.next = None
            else:
                current.next = current.next.next
        current = current.next
    return head


print("Problem 7:")
slingshot = Node("Slingshot")
peaches = Node("Peaches")
beetle = Node("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

# Linked List: slingshot -> peaches -> beetle
print_linked_list(delete_item(slingshot, "Peaches"))

# Linked List: slingshot -> beetle
print_linked_list(delete_item(slingshot, "Triceratops Torso"))
print()
