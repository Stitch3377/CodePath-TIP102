"""
Session 1: Unit 1
Breakout Problem Set - Standard Version 1
"""


def welcome():
    """Problem 1"""
    print("Welcome to The Hundred Acre Wood!")


print("Problem 1:")
welcome()
print()


def greeting(name):
    """Problem 2"""
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Iv.")


print("Problem 2:")
greeting("bob")
print()


def print_catchphrase(character):
    """Problem 3"""
    match character:
        case "Pooh":
            print("Oh bother!")
        case "Tigger":
            print("TTFN: Ta-ta for now!")
        case "Eeyore":
            print("Thanks for noticing me.")
        case "Christopher Robin":
            print("Silly old bear.")
        case _:
            print(f"Sorry! I don't know {character}'s catchphrase!")


print("Problem 3:")
print_catchphrase("Pooh")
print_catchphrase("Piglet")
print()


def get_item(items, x):
    """Problem 4"""
    if x >= len(items):
        return None
    return items[x]


print("Problem 4:")
items = ["piglet", "pooh", "roo", "rabbit"]
result = get_item(items, 2)
print(result)

items = ["piglet", "pooh", "roo", "rabbit"]
result = get_item(items, 5)
print(result)
print()


def sum_honey(hunny_jars):
    """Problem 5"""
    sum = 0
    for jar in hunny_jars:
        sum += jar
    return sum


print("Problem 5:")
hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))
print()


def doubled(hunny_jars):
    """Problem 6"""
    return [jar * 2 for jar in hunny_jars]


print("Problem 6:")
hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))
print()


def count_less_than(race_times, threshold):
    """Problem 7"""
    count = 0
    for time in race_times:
        if time < threshold:
            count += 1
    return count


print("Problem 7:")
race_times = [1, 2, 3, 4, 5, 6]
print(count_less_than(race_times, 4))

race_times = []
print(count_less_than(race_times, 4))
print()


def print_todo_list(task):
    """Problem 8"""
    print("Pooh's To Dos:")
    for num, item in enumerate(task):
        print(f"{num+1}. {item}")


print("Problem 8:")
tasks = [
    "Count all the bees in the hive",
    "Chase all the clouds from the sky",
    "Think",
    "Stoutness Exercises",
]
print_todo_list(tasks)

tasks = []
print_todo_list(tasks)
print("")


def can_pair(item_quantities):
    """Problem 9"""
    for quantity in item_quantities:
        if quantity % 2 != 0:
            return False
    return True


print("Problem 9:")
item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))
print()


def split_haycorns(quantity):
    """Problem 10"""
    result = []
    for i in range(1, quantity + 1):
        if quantity % i == 0:
            result.append(i)
    print(result)


print("Problem 10:")
split_haycorns(6)
split_haycorns(1)
print()


def tiggerfy(s):
    """Problem 11"""
    tiger = ["t", "i", "g", "e", "r"]
    result = ""
    for letter in s.lower():
        if letter not in tiger:
            result += letter
    print(result)


print("Problem 11:")
tiggerfy("suspicerous")
tiggerfy("Trigger")
tiggerfy("Hunny")
print()


def locate_thistles(items):
    """Problem 12"""
    result = []
    for i, item in enumerate(items):
        if "thistle" in item:
            result.append(i)
    print(result)


print("Problem 12:")
items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)
print()
