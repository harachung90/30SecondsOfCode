def in_range(n, start, end=0):
    return start <= n <= end if end >= start else end <= n <= start

in_range(3, 2, 5) # True
in_range(3, 4) # True
in_range(2, 3, 5) # False
in_range(3, 2) # False

print(in_range(3, 2, 5))
print(in_range(3, 4))
print(in_range(2, 3, 5))
print(in_range(3, 2))
