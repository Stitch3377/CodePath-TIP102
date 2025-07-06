"""
Session 6: Unit 3
Breakout Problem Set - Standard Version 1
"""


def manage_stage_changes(changes):
    """Problem 1"""
    performance = []
    cancelled = []
    for action in changes:
        if "Schedule" in action:
            performance.append(action[-1])
        elif action == "Cancel":
            cancelled.append(performance.pop())
        elif action == "Reschedule":
            try:
                cancelled_perf = cancelled.pop()
            except IndexError:
                cancelled_perf = None
            if cancelled_perf is not None:
                performance.append(cancelled_perf)
    return performance


print("Problem 1:")
print(
    manage_stage_changes(
        ["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]
    )
)
print(
    manage_stage_changes(
        ["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"]
    )
)
print(
    manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])
)
print()


def process_performance_requests(requests):
    """Problem 2"""
    queue = []
    requests.sort(reverse=True)
    for perf in requests:
        queue.append(perf[1])
    return queue


print("Problem 2:")
print(process_performance_requests([(3, "Dance"), (5, "Music"), (1, "Drama")]))
print(
    process_performance_requests(
        [(2, "Poetry"), (1, "Magic Show"), (4, "Concert"), (3, "Stand-up Comedy")]
    )
)
print(
    process_performance_requests(
        [
            (1, "Art Exhibition"),
            (3, "Film Screening"),
            (2, "Workshop"),
            (5, "Keynote Speech"),
            (4, "Panel Discussion"),
        ]
    )
)
print()


def collect_festival_points(points):
    """Problem 3"""
    stack = []
    total = 0
    for booth in points:
        stack.append(booth)
        total += stack[-1]
    return total


print("Problem 3:")
print(collect_festival_points([5, 8, 3, 10]))
print(collect_festival_points([2, 7, 4, 6]))
print(collect_festival_points([1, 5, 9, 2, 8]))
print()


def booth_navigation(clues):
    """Problem 4"""
    stack = []
    for clue in clues:
        if clue != "back":
            stack.append(clue)
        else:
            if stack:
                stack.pop()
    return stack


print("Problem 4:")
booth_clues = [1, 2, "back", 3, 4]
print(booth_navigation(booth_clues))

booth_clueses = [5, 3, 2, "back", "back", 7]
print(booth_navigation(booth_clues))

booth_clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(booth_clues))
print()


def merge_schedules(schedule1, schedule2):
    """Problem 5"""
    pointer1 = 0
    pointer2 = 0
    result = ""

    while pointer1 < len(schedule1) and pointer2 < len(schedule2):
        result += schedule1[pointer1]
        result += schedule2[pointer2]
        pointer1 += 1
        pointer2 += 1
    while pointer1 < len(schedule1):
        result += schedule1[pointer1]
        pointer1 += 1
    while pointer2 < len(schedule2):
        result += schedule2[pointer2]
        pointer2 += 1

    return result


print("Problem 5:")
print(merge_schedules("abc", "pqr"))
print(merge_schedules("ab", "pqrs"))
print(merge_schedules("abcd", "pq"))
print()


def next_greater_event(schedule1, schedule2):
    """Problem 6"""
    stack = []
    greater = {}

    for event_pop in reversed(schedule2):
        while stack and stack[-1] <= event_pop:
            stack.pop()
        greater[event_pop] = stack[-1] if stack else -1
        stack.append(event_pop)

    return [greater[num] for num in schedule1]


print("Problem 6:")
print(next_greater_event([4, 1, 2], [1, 3, 4, 2]))
print(next_greater_event([2, 4], [1, 2, 3, 4]))
print()


def sort_performances_by_type(performances):
    """Problem 7"""
    left = 0
    right = len(performances) - 1

    while left < right:
        if performances[left] % 2 == 0:
            left += 1
        elif performances[right] % 2 == 1:
            right -= 1
        else:
            old_left = performances[left]
            old_right = performances[right]
            performances[left] = old_right
            performances[right] = old_left
            left += 1
            right -= 1
    return performances


print("Problem 7:")
print(sort_performances_by_type([3, 1, 2, 4]))
print(sort_performances_by_type([0]))
print()
