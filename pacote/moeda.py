def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


if __name__ == '__main__':
    print(moeda(10.50))
