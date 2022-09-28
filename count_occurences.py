def count_occurences(lst, val):
    return len([x for x in lst if x == val and type(x)  == type(val)])


count_occurences([1, 1, 2, 1, 2, 3], 1) #3

print(count_occurences([1, 1, 2, 1, 2, 3], 1))