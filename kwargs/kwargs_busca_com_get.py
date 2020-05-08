def func(*args, **kwargs):
    print(args)
    name = kwargs.get('nome')
    idade = kwargs.get('idade')
    print(f'Nome:{name} \nIdade: {idade} anos')


lista1 = [1, 2, 3]

func(*lista1, nome='Jean', sobrenome='Charlles', idade=50)
