def take_right(itr, n=1):
    return itr[-n:]


take_right([1, 2, 3], 2) # [2, 3]
take_right([1, 2, 3]) # [3]

print(take_right([1, 2, 3], 2))
print(take_right([1, 2, 3]))