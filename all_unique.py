def all_unique(lst):
    return len(lst) == len(set(lst))

#Examples
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]

all_unique(x) #True
all_unique(y) #False

print(all_unique(x))
print(all_unique(y))