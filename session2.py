"""
Session 2: Unit 1
Breakout Problem Set - Standard Version 1
"""


def reverse_sentence(sentence):
    """Problem 1"""
    reversed_words = sentence.split()[::-1]
    return " ".join(reversed_words)


print("Problem 1:")
sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))
print()


def goldilocks_approved(nums):
    """Problem 2"""
    max_num = max(nums)
    min_num = min(nums)

    for num in nums:
        if num != max_num and num != min_num:
            return num
    return -1


print("Problem 2:")
nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))
print()


def delete_minimum_elements(hunny_jar_sizes):
    """Problem 3"""
    result = []
    while hunny_jar_sizes:
        smallest_jar = min(hunny_jar_sizes)
        result.append(smallest_jar)
        hunny_jar_sizes.remove(smallest_jar)
    return result


print("Problem 3:")
hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))
print("")


def sum_of_digits(num):
    """Problem 4"""
    sum = 0
    while num != 0:
        remainder = num % 10
        num = (num - remainder) // 10
        sum += remainder
    return sum


print("Problem 4")
print(sum_of_digits(423))
print(sum_of_digits(4))
print()


def final_value_after_operations(operations):
    tigger = 1
    for operation in operations:
        match (operation):
            case "trouncy" | "pouncy":
                tigger -= 1
            case "bouncy" | "flouncy":
                tigger += 1
    return tigger


print("Problem 5:")
print(final_value_after_operations(["trouncy", "flouncy", "flouncy"]))
print(final_value_after_operations(["bouncy", "bouncy", "flouncy"]))
print()


def is_acronym(words, s):
    """Problem 6"""
    maybe_acronym = ""
    for word in words:
        maybe_acronym += word[0]
    return maybe_acronym == s


print("Problem 6:")
print(is_acronym(["christopher", "robin", "milne"], "crm"))
print()


def make_divisible_by_3(nums):
    """Problem 7"""
    count = 0
    for num in nums:
        if num % 3 == 0:
            count += 1
    return len(nums) - count


print("Problem 7:")
print(make_divisible_by_3([1, 2, 3, 4]))
print(make_divisible_by_3([3, 6, 9]))
print()


def exclusive_elements(lst1, lst2):
    """Problem 8"""
    set1 = set(lst1)
    set2 = set(lst2)
    return list(set1.difference(set2).union(set2.difference(set1)))


print("Problem 8:")
lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elements(lst1, lst2))

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elements(lst1, lst2))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elements(lst1, lst2))
print()


def merge_alternately(word1, word2):
    """Problem 9"""
    merged = ""
    i = 0
    j = 0
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            merged += word1[i]
            i += 1
        if j < len(word2):
            merged += word2[j]
            j += 1
    return merged


print("Problem 9:")
word1 = "wol"
word2 = "oze"
print(merge_alternately(word1, word2))

word1 = "hfa"
word2 = "eflump"
print(merge_alternately(word1, word2))

word1 = "eyre"
word2 = "eo"
print(merge_alternately(word1, word2))
print()


def good_pairs(pile1, pile2, k):
    """Problem 10"""
    count = 0
    for item1 in pile1:
        for item2 in pile2:
            if item1 % (item2 * k) == 0:
                count += 1
    return count


print("Problem 10:")
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
print(good_pairs(pile1, pile2, 1))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
print(good_pairs(pile1, pile2, 3))
print()
