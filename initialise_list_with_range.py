def initialise_list_with_range(end, start=0, step=1):
    return list(range(start, end + 1, step))


initialise_list_with_range(5) # [0, 1, 2, 3, 4, 5]
initialise_list_with_range(7, 3) # [3, 4, 5, 6, 7]
initialise_list_with_range(9, 0, 2) # [0, 2, 4, 6, 8]

print(initialise_list_with_range(5))
print(initialise_list_with_range(7, 3))
print(initialise_list_with_range(9, 0, 2))