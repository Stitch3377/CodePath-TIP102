"""
Session 19: Unit 10
Breakout Problem Set - Standard Version 1
"""

"""
JFK ----- LAX
|
|
DFW ----- ATL
"""

flights = {}
flights["JFK"] = ["LAX", "DFW"]
flights["LAX"] = ["JFK"]
flights["DFW"] = ["ATL", "JFK"]
flights["ATL"] = ["DFW"]

print("Problem 1:")
print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])
print()


def bidirectional_flights(flights):
    """Problem 2"""
    for i in range(len(flights) - 1):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True


print("Problem 2:")
flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))
print()


def get_direct_flights(flights, source):
    """Problem 3"""
    results = []

    for idx, dest in enumerate(flights[source]):
        if dest == 1:
            results.append(idx)

    return results


print("Problem 3:")
flights = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0]]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))
print()


def get_adj_dict(flights):
    """Problem 4"""
    result = {}

    for edge in flights:
        a = edge[0]
        b = edge[1]
        result.setdefault(a, []).append(b)
        result.setdefault(b, []).append(a)
    return result


print("Problem 4:")
flights = [
    ["Cape Town", "Addis Ababa"],
    ["Cairo", "Lagos"],
    ["Lagos", "Addis Ababa"],
    ["Nairobi", "Cairo"],
    ["Cairo", "Cape Town"],
]
print(get_adj_dict(flights))
print()
