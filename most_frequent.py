def most_frequent(list):
    return max(set(list), key=list.count)


most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]) # 2

print(most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]))