def min_n(lst, n=1):
    return sorted(lst, reverse=False)[:n]


min_n([1, 2, 3]) # [1]
min_n([1, 2, 3], 2) # [1, 2]
min_n([3, 7, 0, 5, 4, 2], 3) # [0, 2, 3]

print(min_n([1, 2, 3]))
print(min_n([1, 2, 3], 2))
print(min_n([3, 7, 0, 5, 4, 2], 3))
