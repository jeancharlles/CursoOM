def func(*args):
    print(args)


lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

func(*lista1, *lista2)
