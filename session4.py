"""
Session 4: Unit 2
Breakout Problem Set - Standard Version 2
"""


def remove_low_rated_destinations(destinations, rating_threshold):
    """Problem 1"""
    updated = {}
    for dest, rating in destinations.items():
        if rating >= rating_threshold:
            updated[dest] = rating
    return updated


print("Problem 1:")
destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogotá": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}
print(remove_low_rated_destinations(destinations, 4.0))
print(remove_low_rated_destinations(destinations2, 4.9))
print()


def unique_souvenir_counts(souvenirs):
    """Problem 2"""
    map = {}
    for s in souvenirs:
        if s in map:
            map[s] += 1
        else:
            map[s] = 1
    return len(set(map.values())) == len(map.values())


print("Problem 2:")
souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]
souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]

print(unique_souvenir_counts(souvenirs1))
print(unique_souvenir_counts(souvenirs2))
print(unique_souvenir_counts(souvenirs3))
print()


def decode_message(key, message):
    """Problem 3"""
    message_dict = {}
    letter = 97
    for char in key:
        if char in message_dict.keys() or char == " ":
            pass
        else:
            message_dict[char] = letter
            letter += 1

    decoded = ""
    for char in message:
        if char == " ":
            decoded += " "
        else:
            decoded += chr(message_dict[char])

    return decoded


print("Problem 3:")
key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"

print(decode_message(key1, message1))

key2 = "eljuxhpwnyrdgtqkviszcfmabo"
message2 = "hntu depcte lxejw lxwntu zwx piqfx"

print(decode_message(key2, message2))
print()


def find_longest_harmonious_travel_sequence(ratings):
    """Problem 4"""
    # Initialize a dictionary to store the frequency of each rating
    frequency = {}

    # Count the occurrences of each rating
    for rating in ratings:
        if rating in frequency:
            frequency[rating] += 1
        else:
            frequency[rating] = 1
    max_length = 0

    # Find the longest harmonious sequence
    for rating in frequency:
        if rating + 1 in frequency:
            max_length = max(max_length, frequency[rating] + frequency[rating + 1])

    return max_length


print("Problem 4:")
durations1 = [1, 3, 2, 2, 5, 2, 3, 7]
durations2 = [1, 2, 3, 4]
durations3 = [1, 1, 1, 1]

print(find_longest_harmonious_travel_sequence(durations1))
print(find_longest_harmonious_travel_sequence(durations2))
print(find_longest_harmonious_travel_sequence(durations3))
print()


def is_route_covered(trips, start_dest, end_dest):
    route = set(range(start_dest, end_dest + 1))

    for start, end in trips:
        for destination in range(start, end + 1):
            if destination in route:
                route.remove(destination)

    return len(route) == 0


print("Problem 5:")
trips1 = [[1, 2], [3, 4], [5, 6]]
start_dest1, end_dest1 = 2, 5

trips2 = [[1, 10], [10, 20]]
start_dest2, end_dest2 = 21, 21

trips3 = [[1, 2], [3, 5]]
start_dest3, end_dest3 = 2, 5

print(is_route_covered(trips1, start_dest1, end_dest1))
print(is_route_covered(trips2, start_dest2, end_dest2))
print(is_route_covered(trips3, start_dest3, end_dest3))
print()


def most_popular_even_destination(destinations):
    """Problem 6"""
    freq = {}

    for dest in destinations:
        if dest % 2 == 0:
            if dest in freq:
                freq[dest] += 1
            else:
                freq[dest] = 1

    if freq:
        pop_dest = max(freq, key=freq.get)
    else:
        return -1

    if freq[pop_dest] == 1:
        return -1
    else:
        return pop_dest


print("Problem 6:")
destinations1 = [0, 1, 2, 2, 4, 4, 1]
destinations2 = [4, 4, 4, 9, 2, 4]
destinations3 = [29, 47, 21, 41, 13, 37, 25, 7]

print(most_popular_even_destination(destinations1))
print(most_popular_even_destination(destinations2))
print(most_popular_even_destination(destinations3))
print()


def is_valid_itinerary(itinerary):
    """Problem 7"""
    n = max(itinerary)

    if len(itinerary) != (n + 1):
        return False

    freq = {}
    for city in itinerary:
        if city in freq:
            freq[city] += 1
        else:
            freq[city] = 1

    for i in range(1, n):
        if freq.get(i) != 1:
            return False

    return freq.get(n) == 2


print("Problem 7:")
itinerary1 = [2, 1, 3]
itinerary2 = [1, 3, 3, 2]
itinerary3 = [1, 1]

print(is_valid_itinerary(itinerary1))
print(is_valid_itinerary(itinerary2))
print(is_valid_itinerary(itinerary3))
print()


def find_attractions(tourist_list1, tourist_list2):
    """Problem 8"""
    set1 = set(tourist_list1)
    set2 = set(tourist_list2)

    common_attractions = set1 & set2

    travel_times = {}
    for attraction in common_attractions:
        travel_times[attraction] = tourist_list1.index(
            attraction
        ) + tourist_list2.index(attraction)

    min_travel_time = min(travel_times.values())

    return [
        attraction
        for attraction, value in travel_times.items()
        if value == min_travel_time
    ]


print("Problem 8:")
tourist_list1 = ["Eiffel Tower", "Louvre Museum", "Notre-Dame", "Disneyland"]
tourist_list2 = ["Colosseum", "Trevi Fountain", "Pantheon", "Eiffel Tower"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["Eiffel Tower", "Louvre Museum", "Notre-Dame", "Disneyland"]
tourist_list2 = ["Disneyland", "Eiffel Tower", "Notre-Dame"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["beach", "mountain", "forest"]
tourist_list2 = ["mountain", "beach", "forest"]

print(find_attractions(tourist_list1, tourist_list2))
print()
