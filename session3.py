"""
Session 3: Unit 2
Breakout Problem Set - Standard Version 2
"""


def space_crew(crew, position):
    """Problem 1"""
    result = {}
    for i, member in enumerate(crew):
        result[member] = position[i]
    return result


print("Problem 1:")
exp70_crew = [
    "Andreas Mogensen",
    "Jasmin Moghbeli",
    "Satoshi Furukawa",
    "Loral O'Hara",
    "Konstantin Borisov",
]
exp70_positions = [
    "Commander",
    "Flight Engineer",
    "Flight Engineer",
    " Flight Engineer",
    "Flight Engineer",
]

ax3_crew = [
    "Michael Lopez-Alegria",
    "Walter Villadei",
    "Alper Gezeravci",
    "Marcus Wandt",
]
ax3_positions = [
    "Commander",
    "Mission Pilot",
    "Mission Specialist",
    "Mission Specialist",
]
print(space_crew(exp70_crew, exp70_positions))
print(space_crew(ax3_crew, ax3_positions))
print()


def planet_lookup(planet_name):
    """Problem 2"""
    planetary_info = {
        "Mercury": {"Moons": 0, "Orbital Period": 88},
        "Earth": {"Moons": 1, "Orbital Period": 365.25},
        "Mars": {"Moons": 2, "Orbital Period": 687},
        "Jupiter": {"Moons": 79, "Orbital Period": 10592},
    }

    result = planetary_info.get(planet_name, 0)
    if result == 0:
        return "Sorry, I have no data on that planet"
    else:
        moons = planetary_info[planet_name]["Moons"]
        orbit = planetary_info[planet_name]["Orbital Period"]
        return "Planet {name} has an orbital period of {orbit} Earth days and has {moons} moons.".format(
            name=planet_name, moons=moons, orbit=orbit
        )


print("Problem 2:")
print(planet_lookup("Jupiter"))
print(planet_lookup("Pluto"))
print()


def check_oxygen_levels(oxygen_levels, min_val, max_val):
    """Problem 3"""
    result = []
    for room, level in oxygen_levels.items():
        if level < min_val or level > max_val:
            result.append(room)
    return result


print("Problem 3")
oxygen_levels = {
    "Command Module": 21,
    "Habitation Module": 20,
    "Laboratory Module": 19,
    "Airlock": 22,
    "Storage Bay": 18,
}
print(check_oxygen_levels(oxygen_levels, 19, 22))
print()


def data_difference(experiment1, experiment2):
    """Problem 4"""
    result = {}

    for k, v in experiment1.items():
        if k not in experiment2.keys():
            result[k] = v
        if k in experiment2.keys():
            if experiment1[k] != experiment2[k]:
                result[k] = v
    return result


print("Problem 4:")
exp1_data = {"temperature": 22, "pressure": 101.3, "humidity": 45}
exp2_data = {"temperature": 18, "pressure": 101.3, "radiation": 0.5}
print(data_difference(exp1_data, exp2_data))
print()


def get_winner(votes):
    """Problem 5"""
    freq = {}

    for vote in votes:
        if vote in freq:
            freq[vote] += 1
        else:
            freq[vote] = 1

    return max(freq, key=freq.get)


print("Problem 5:")
votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]
print(get_winner(votes1))
print(get_winner(votes2))
print()


def check_if_complete_transmission(transmission):
    """
    Problem 6
    :type transmission: str
    :rtype: bool
    """
    for char in transmission.lower():
        if not char.isalpha:
            return False
    return len(set(transmission.lower())) == 26


print("Problem 6:")
transmission1 = "thequickbrownfoxjumpsoverthelazydog"
transmission2 = "spacetravel"
print(check_if_complete_transmission(transmission1))
print(check_if_complete_transmission(transmission2))
print()


def max_number_of_string_pairs(signals):
    """Problem 7"""
    pair_count = 0
    unmatched = set()

    for signal in signals:
        reversed_signal = signal[::-1]
        if reversed_signal in unmatched:
            pair_count += 1
            unmatched.remove(reversed_signal)
        else:
            unmatched.add(signal)
    return pair_count


print("Problem 7:")
signals1 = ["cd", "ac", "dc", "ca", "zz"]
signals2 = ["ab", "ba", "cc"]
signals3 = ["aa", "ab"]
print(max_number_of_string_pairs(signals1))
print(max_number_of_string_pairs(signals2))
print(max_number_of_string_pairs(signals3))
print()


def find_difference(signals1, signals2):
    """Problem 8"""
    set1 = set(signals1)
    set2 = set(signals2)

    diff1 = set1.difference(set2)
    diff2 = set2.difference(set1)

    return [list(diff1), list(diff2)]


print("Problem 8:")
signals1_example1 = [1, 2, 3]
signals2_example1 = [2, 4, 6]

signals1_example2 = [1, 2, 3, 3]
signals2_example2 = [1, 1, 2, 2]

print(find_difference(signals1_example1, signals2_example1))
print(find_difference(signals1_example2, signals2_example2))
print()


def find_common_signals_dict(signals1, signals2):
    """Problem 9"""
    dict2 = {val: True for val in signals2}
    dict1 = {val: True for val in signals1}
    answer1 = sum(1 for val in signals1 if val in dict2)
    answer2 = sum(1 for val in signals2 if val in dict1)
    return [answer1, answer2]


print("Problem 9:")
signals1_example1 = [2, 3, 2]
signals2_example1 = [1, 2]
print(find_common_signals_dict(signals1_example1, signals2_example1))

signals1_example2 = [4, 3, 2, 3, 1]
signals2_example2 = [2, 2, 5, 2, 3, 6]
print(find_common_signals_dict(signals1_example2, signals2_example2))

signals1_example3 = [3, 4, 2, 3]
signals2_example3 = [1, 5]
print(find_common_signals_dict(signals1_example3, signals2_example3))
print()


def find_common_signals_set(signals1, signals2):
    """Problem 10"""
    set2 = set(signals2)
    set1 = set(signals1)
    answer1 = sum(1 for val in signals1 if val in set2)
    answer2 = sum(1 for val in signals2 if val in set1)
    return [answer1, answer2]


print("Problem 10:")
signals1_example1 = [2, 3, 2]
signals2_example1 = [1, 2]
print(find_common_signals_set(signals1_example1, signals2_example1))

signals1_example2 = [4, 3, 2, 3, 1]
signals2_example2 = [2, 2, 5, 2, 3, 6]
print(find_common_signals_set(signals1_example2, signals2_example2))

signals1_example3 = [3, 4, 2, 3]
signals2_example3 = [1, 5]
print(find_common_signals_set(signals1_example3, signals2_example3))
print()


# FIX THIS LATER
def frequency_sort(signals):
    """Problem 11"""
    freq = {}
    for signal in signals:
        if signal in freq:
            freq[signal] += 1
        else:
            freq[signal] = 0

    sorted_signals = sorted(signals, key=lambda x: (freq[x], x))

    return sorted_signals


print("Problem 11:")
signals1 = [1, 1, 2, 2, 2, 3]
signals2 = [2, 3, 1, 3, 2]
signals3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]

print(frequency_sort(signals1))
print(frequency_sort(signals2))
print(frequency_sort(signals3))
print()
