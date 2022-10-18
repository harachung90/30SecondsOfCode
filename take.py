def take(itr, n=1):
    return itr[:n]


take([1, 2, 3], 5)  # [1,2,3]
take([1, 2, 3], 0)  # []

print(take([1, 2, 3], 5))
print(take([1, 2, 3], 0))