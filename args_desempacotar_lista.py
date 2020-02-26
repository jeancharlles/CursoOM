def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))


lista = [1, 2, 3]
# func(lista)
func(*lista)
