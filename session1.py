"""Session 1"""


# Problem 1
def welcome():
    print("Welcome to The Hundred Acre Wood!")


welcome()


# Problem 2
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Iv.")


greeting("bob")


# Problem 3
def print_catchphrase(character):
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


print_catchphrase("Pooh")
print_catchphrase("Piglet")


# Problem 4
def get_item(items, x):
    if x >= len(items):
        return None
    return items[x]


items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
result = get_item(items, x)
print(result)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
result = get_item(items, x)
print(result)


# Problem 5
def sum_honey(hunny_jars):
    sum = 0
    for jar in hunny_jars:
        sum += jar
    return sum


hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))


# Problem 6
def doubled(hunny_jars):
    return [jar * 2 for jar in hunny_jars]


hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))


# Problem 7
def count_less_than(race_times, threshold):
    count = 0
    for time in race_times:
        if time < threshold:
            count += 1
    return count


race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))
