def max_by(lst, fn):
    return max(map(fn, lst))

max_by([
    {'n': 4},
    {'n': 2},
    {'n': 8},
    {'n': 6},
], lambda v : v['n']) # 8

print(max_by([
    {'n': 4},
    {'n': 2},
    {'n': 8},
    {'n': 6},
], lambda v : v['n']))