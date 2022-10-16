from random import randint


def sample(lst):
    return lst[randint(0, len(lst) - 1)]

sample([3, 7, 9, 11])

print(sample([3, 7, 9, 11]))