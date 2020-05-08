lista = [['P1', 10], ['P2', 5], ['P3', 18], ['P4', 9], ['P5', 12]]


def func(item):
    return item[1]  # [0] são strings e [1] são valores


lista.sort(key=func)  # ordem crescente
# lista.sort(key=func, reverse=True)  # ordem decrescente

print(lista)
