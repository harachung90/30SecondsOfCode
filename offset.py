def offset(lst, offset):
    return lst[offset:] + lst[:offset]


offset([1, 2, 3, 4, 5], 2)  # [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2)  # [4, 5, 1, 2, 3]

print(offset([1, 2, 3, 4, 5], 2))
print(offset([1, 2, 3, 4, 5], -2))