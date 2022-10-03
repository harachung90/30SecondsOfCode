from collections import Counter

def filter_unique(lst):
    return [item for item, count in Counter(lst).items() if count > 1]


filter_unique([1, 2, 2, 3, 4, 4, 5]) # [2,4]

print(filter_unique([1, 2, 2, 3, 4, 4, 5]))