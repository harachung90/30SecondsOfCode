from collections import Counter


def filter_non_unique(lst):
    return [item for item, count in Counter(lst).items() if count == 1]


filter_non_unique([1, 2, 2, 3, 4, 4, 5])  # [1, 3, 5]

print(filter_non_unique([1, 2, 2, 3, 4, 4, 5]))