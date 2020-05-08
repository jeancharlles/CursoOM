# Esta função é um gerador

import time


def gerador():

    for n in range(10):
        yield n
        time.sleep(0.1)


g = gerador()

print(next(g))
print(next(g))
print(next(g))

print(hasattr(g, '__next__'))
print(hasattr(g, '__iter__'))

