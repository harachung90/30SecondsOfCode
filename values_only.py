def values_only(flat_dict):
    return list(flat_dict.values())


ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9
}

values_only(ages) # [10, 11, 0]

print(values_only(ages) )