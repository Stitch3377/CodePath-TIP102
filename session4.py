# Problem 1
# Inputs: destinations (dict), rating threshold (number)
# Outputs: update dictionary with destinations > rating threshold
# Constraints: n/a
# Edge cases: negative ratings, empty ratings/dict
def remove_low_rated_destinations(destinations, rating_threshold):
    updated = {}
    for dest, rating in destinations.items():
        if rating >= rating_threshold:
            updated[dest] = rating
    return updated


destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogotá": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}

# print(remove_low_rated_destinations(destinations, 4.0))
# print(remove_low_rated_destinations(destinations2, 4.9))


# Problem 2
# Understand
#   Inputs: array of souveneirs
#   Outputs: boolean, if souveneir occurrence is unique or not
#   Constraints: n/a
#   Edge cases: empty array
# Plan
#   cast to a set
#   check if the set length is the same as the array length
def unique_souvenir_counts(souvenirs):
    map = {}
    for s in souvenirs:
        if s in map:
            map[s] += 1
        else:
            map[s] = 1
    return len(set(map.values())) == len(map.values())


souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]
souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]

# print(unique_souvenir_counts(souvenirs1))
# print(unique_souvenir_counts(souvenirs2))
# print(unique_souvenir_counts(souvenirs3))


# Problem 3
# Understand
#   Inputs: key, encoded message
#   Outputs: decoded message
#   Constraints:
#   Edge cases:
# Plan
def decode_message(key, message):
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


# key1 = "the quick brown fox jumps over the lazy dog"
# message1 = "vkbs bs t suepuv"

# print(decode_message(key1, message1))

# key2 = "eljuxhpwnyrdgtqkviszcfmabo"
# message2 = "hntu depcte lxejw lxwntu zwx piqfx"

# print(decode_message(key2, message2))

# Problem 4
# Understand
#   Inputs:
#   Outputs:
#   Constraints:
#   Edge cases:
# Plan
