def longest_item(*args):
    return max(args, key = len)


longest_item('this', 'is', 'a', 'testcase')  # 'testcase'
longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5])  # [1, 2, 3, 4, 5]
longest_item([1, 2, 3], 'foobar')  # foobar

print(longest_item('this', 'is', 'a', 'testcase'))
print(longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]))
print(longest_item([1, 2, 3], 'foobar'))