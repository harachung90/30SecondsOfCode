def for_each_right(itr, fn):
    for el in itr[::-1]:
        fn(el)


for_each_right([1, 2,3], print) # 3 2 1