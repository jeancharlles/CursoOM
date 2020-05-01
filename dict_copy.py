import copy

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': ['lal', 'bla']}
v = copy.deepcopy(d1)

print('d1', d1)
print(v)

v['a'] = 2

print(d1)
print(v)
