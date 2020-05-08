def func(*args, **kwargs):
    print(args)
    print(kwargs)


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

func(*lista1, *lista2, *lista3, 10, nome='Jean', sobrenome='Charlles')
