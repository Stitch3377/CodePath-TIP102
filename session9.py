class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and all(
            c.isalpha() or c.isspace() for c in new_catchphrase
        ):
            self.catchphrase = new_catchphrase
            print("Catchphrase Updated")
        else:
            print("Invalid catchphrase")

    def add_item(self, item_name):
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


apollo = Villager("Apollo", "Eagle", "pah")

# print(apollo.name)
# print(apollo.species)
# print(apollo.catchphrase)
# print(apollo.furniture)

bones = Villager("Bones", "Dog", "yip yip")

# print(bones.name)
# print(bones.species)
# print(bones.catchphrase)
# print(bones.furniture)
# print(bones.greet_player("Tram"))

bones.catchphrase = "ruff it up"

# print(bones.greet_player("Samia"))


# alice = Villager("Alice", "Koala", "guvnor")
# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
# print(alice.catchphrase)

alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)
alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()
