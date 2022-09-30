def drop(a, n=1):
    return a[n:]


drop([1, 2, 3])  # [2, 3]
drop([1, 2, 3], 2)  # [3]
drop([1, 2, 3], 42)  # []

print(drop([1, 2, 3]))
print(drop([1, 2, 3], 2))
print(drop([1, 2, 3], 42))
