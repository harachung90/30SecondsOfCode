def tail(lst):
    return lst[1:] if len(lst) > 1 else lst


tail([1, 2, 3]) # [2, 3]
tail([1]) # [1]

print(tail([1, 2, 3]))
print(tail([1]))