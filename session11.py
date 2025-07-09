"""
Session 11: Unit 6
Breakout Problem Set - Standard Version 1
"""


class SongNode:
    """Problem 1 SongNode class"""

    def __init__(self, song, next=None):
        self.song = song
        self.next = next


# For testing
def print_linked_list(node):
    """Print linked list for problem 1"""
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()


# top_hits_2010s = SongNode(
#     "Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance"))
# )

bad_romance = SongNode("Bad Romance")
party_rock = SongNode("Party Rock Anthem", bad_romance)
uptown_funk = SongNode("Uptown Funk", party_rock)
top_hits_2010s = uptown_funk

print("Problem 1:")
print_linked_list(top_hits_2010s)
print()


class SongNode2:
    """Problem 2-4 SongNode class"""

    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next


def get_artist_frequency(playlist):
    """Problem 2"""
    artist_freq = {}

    current = playlist
    while current:
        if current.artist in artist_freq:
            artist_freq[current.artist] += 1
        else:
            artist_freq[current.artist] = 1
        current = current.next

    return artist_freq


print("Problem 2:")
playlist = SongNode2(
    "Saturn",
    "SZA",
    SongNode2(
        "Who",
        "Jimin",
        SongNode2("Espresso", "Sabrina Carpenter", SongNode2("Snooze", "SZA")),
    ),
)
print(get_artist_frequency(playlist))
print()


def print_linked_list2(node):
    "Print linked list for problem 3-4"
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


# Function with a bug!
def remove_song(playlist_head, song):
    """Problem 3"""
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next
            return playlist_head
        current = current.next
    return playlist_head


print("Problem 3:")
playlist = SongNode2(
    "SOS",
    "ABBA",
    SongNode2(
        "Simple Twist of Fate",
        "Bob Dylan",
        SongNode2("Dreams", "Fleetwood Mac", SongNode2("Lovely Day", "Bill Withers")),
    ),
)
print_linked_list2(remove_song(playlist, "Dreams"))
print()


def on_repeat(playlist_head):
    """Problem 4"""
    if not playlist_head:
        return False

    slow = playlist_head
    fast = playlist_head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False


print("Problem 4:")
song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))
print()


def loop_length(playlist_head):
    """Problem 5"""
    slow = playlist_head
    fast = playlist_head

    # Detect the cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            current = slow.next
            cycle_length = 1
            while current != slow:
                current = current.next
                cycle_length += 1
            return cycle_length
    return 0


print("Problem 5:")
song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))
print()
