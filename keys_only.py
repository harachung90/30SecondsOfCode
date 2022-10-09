def keys_only(flat_dict):
    return list(flat_dict.keys())

ages = {
    "Lexy": 17,
    "Trip": 16,
    "Moody": 15,
    "Izzy": 14
}

keys_only(ages) # ['Lexy', 'Trip', 'Moody', 'Izzy']

print(keys_only(ages))