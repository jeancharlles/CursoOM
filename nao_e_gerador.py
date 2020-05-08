# Esta função não é um gerador e sim uma função geradora

import time


def func():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r


f = func()

for v in f:
    print(v)
