# Esta função é um gerador

import time


def gerador():

    for n in range(100):
        yield n
        time.sleep(0.1)


g = gerador()

for v in g:
    print(v)

print(hasattr(g, '__next__'))
print(hasattr(g, '__iter__'))

