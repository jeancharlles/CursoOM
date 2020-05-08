def func(*args):
    args = list(args)
    args[0] = 20
    print(args)


func(1, 2, 3)
