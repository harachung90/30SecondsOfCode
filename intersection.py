def intersection(a, b):
    _a, _b = set(a), set(b)
    return list(_a & _b)

intersection([1, 2, 3], [4, 3, 2]) # [2, 3]

print(intersection([1, 2, 3], [4, 3, 2]))