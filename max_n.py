def max_n(lst, n=1):
    return sorted(lst, reverse=True)[:n]


max_n([1, 2, 3]) # [3]
max_n([1, 2, 3], 2) # [3, 2]

print(max_n([1, 2, 3]))
print(max_n([1, 2, 3], 2) )