def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])


lista1 = [1, 2, 3]

func(*lista1, nome='Jean', sobrenome='Charlles', idade=50)
