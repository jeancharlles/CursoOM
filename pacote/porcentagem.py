def aumento(valor, porcentagem):
    aum = valor + valor * porcentagem/100
    return aum


def reducao(valor, porcentagem):
    red = valor - valor * porcentagem/100
    return red


if __name__ == '__main__':
    print(__name__)
    print(aumento(100, 10))
    print(reducao(100, 10))
