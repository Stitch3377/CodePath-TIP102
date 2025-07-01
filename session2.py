def sum_of_digits(num):

    sum = 0

    while num != 0:
        remainder = num % 10
        num = (num - remainder) // 10
        sum += remainder
    print(sum)


sum_of_digits(423)


def final_value_after_operations(operations):
    tigger = 1
    for operation in operations:
        match (operation):
            case "trouncy" | "pouncy":
                tigger -= 1
            case "bouncy" | "flouncy":
                tigger += 1
    print(tigger)


final_value_after_operations(["trouncy", "flouncy", "flouncy"])
final_value_after_operations(["bouncy", "bouncy", "flouncy"])


def is_acronym(words, s):
    maybe_acronym = ""
    for word in words:
        maybe_acronym += word[0]
    print(maybe_acronym == s)


is_acronym(["christopher", "robin", "milne"], "crm")


def make_divisible_by_3(nums):
    count = 0
    for num in nums:
        if num % 3 == 0:
            count += 1
    print(len(nums) - count)


make_divisible_by_3([1, 2, 3, 4])
make_divisible_by_3([3, 6, 9])
