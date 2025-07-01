# Problem 1
def space_crew(crew, position):
    result = {}
    for i, member in enumerate(crew):
        result[member] = position[i]
    return result


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

# print(space_crew(exp70_crew, exp70_positions))
# print(space_crew(ax3_crew, ax3_positions))

# Problem 2
planetary_info = {
    "Mercury": {"Moons": 0, "Orbital Period": 88},
    "Earth": {"Moons": 1, "Orbital Period": 365.25},
    "Mars": {"Moons": 2, "Orbital Period": 687},
    "Jupiter": {"Moons": 79, "Orbital Period": 10592},
}


def planet_lookup(planet_name):
    result = planetary_info.get(planet_name, 0)
    if result == 0:
        return "Sorry, I have no data on that planet"
    else:
        moons = planetary_info[planet_name]["Moons"]
        orbit = planetary_info[planet_name]["Orbital Period"]
        return "Planet {name} has an orbital period of {orbit} Earth days and has {moons} moons.".format(
            name=planet_name, moons=moons, orbit=orbit
        )


# print(planet_lookup("Jupiter"))
# print(planet_lookup("Pluto"))
