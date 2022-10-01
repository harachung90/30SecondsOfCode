def drop_right(a, n=1):
    return a[:-n]


drop_right([1, 2,3]) #[1, 2]
drop_right([1, 2,3], 2) #[1]
drop_right([1, 2,3], 42) #[]

print(drop_right([1, 2,3]))
print(drop_right([1, 2,3], 2))
print(drop_right([1, 2,3], 42))