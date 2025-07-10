"""
Session 9: Unit 5
Breakout Problem Set - Standard Version 1
"""


class Villager:
    """Problems 1-6 Villager class"""

    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        """Problem 2"""
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        """Problem 4"""
        if len(new_catchphrase) < 20 and all(
            c.isalpha() or c.isspace() for c in new_catchphrase
        ):
            self.catchphrase = new_catchphrase
            print("Catchphrase Updated")
        else:
            print("Invalid catchphrase")

    def add_item(self, item_name):
        """Problem 5"""
        valid_items = [
            "acoustic guitar",
            "ironwood kitchenette",
            "rattan armchair",
            "kotatsu",
            "cacao tree",
        ]
        if item_name in valid_items:
            self.furniture.append(item_name)

    def print_inventory(self):
        """Problem 6"""
        freq = {}
        if not self.furniture:
            print("Inventory Empty")
        else:
            for item in self.furniture:
                if item in freq:
                    freq[item] += 1
                else:
                    freq[item] = 1
            inventory_str = ", ".join(
                f"{item}: {count}" for item, count in freq.items()
            )
            print(inventory_str)


print("Problem 1:")
apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name)
print(apollo.species)
print(apollo.catchphrase)
print(apollo.furniture)
print()

print("Problem 2:")
bones = Villager("Bones", "Dog", "yip yip")
print(bones.greet_player("Tram"))
print()

print("Problem 3:")
bones.catchphrase = "ruff it up"
print(bones.greet_player("Samia"))
print()

print("Problem 4:")
alice = Villager("Alice", "Koala", "guvnor")
alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)
print()

print("Problem 5:")
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)
alice.add_item("acoustic guitar")
print(alice.furniture)
alice.add_item("cacao tree")
print(alice.furniture)
alice.add_item("nintendo switch")
print(alice.furniture)
print()


print("Problem 6:")
alice = Villager("Alice", "Koala", "guvnor")
alice.print_inventory()
alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()
print()


class Villager2:
    """Problem 7 Villager class"""

    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []


def of_personality_type(townies, personality_type):
    """Problem 7"""
    result = []
    for villager in townies:
        if villager.personality == personality_type:
            result.append(villager.name)
    return result


print("Probelm 7:")
isabelle = Villager2("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager2("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager2("Stitches", "Cub", "Lazy", "stuffin'")
print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))
print()


class Villager3:
    """Problem 8 Villager class"""

    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor


def message_received(start_villager, target_villager):
    """Problem 8"""
    current = start_villager
    while current:
        if current == target_villager:
            return True
        current = current.neighbor
    return False


print("Problem 8:")
isabelle = Villager3("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager3("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager3("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider
print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))
print()


class Node:
    """Node class"""

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


print("Problem 9:")
tom_nook = Node("Tom Nook")
tommy = Node("Tommy")
tom_nook.next = tommy

print(tom_nook.value)
print(tom_nook.next.value)
print(tommy.value)
print(tommy.next)
print()


print("Problem 10:")
timmy = Node("Timmy")
tom_nook.next = timmy
timmy.next = tommy

print(tom_nook.value)
print(tom_nook.next.value)
print(timmy.value)
print(timmy.next.value)
print(tommy.value)
print(tommy.next)
print()


print("Problem 11:")
saharah = Node("Saharah")
tom_nook.next = None
tommy.next = saharah

print(tom_nook.next)
print(timmy.value)
print(timmy.next.value)
print(tommy.value)
print(tommy.next.value)
print(saharah.value)
print(saharah.next)
print()


def print_list(head):
    """Problem 12"""
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return " -> ".join(values)


print("Problem 12:")
isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")
isabelle.next = saharah
saharah.next = cj
print(print_list(isabelle))
print()
