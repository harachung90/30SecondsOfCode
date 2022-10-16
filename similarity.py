def similarity(a, b):
    return [item for item in a if item in b]


similarity([1, 2, 3], [1, 2, 4])  # [1, 2]

print(similarity([1, 2, 3], [1, 2, 4]))