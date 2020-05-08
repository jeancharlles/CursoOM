import sys

l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
