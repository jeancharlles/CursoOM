def divide(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as erro:
        print('Esta exceção vai para um arquivo Log:', erro)
        raise


try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(f'Esta parte vai para a tela do usuário{error}')
except Exception as error2:
    print(f'{error2}')
