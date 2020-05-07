lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
]

print(lista)

lista = [
    ('chave1', 2),
    ('chave2', 'valor2'),
]

dic = {x: y for x, y in lista}

print(dic)

lista = [
    ('chave1', 2),
    ('chave2', 'valor2'),
]

dic = {x: y*2 for x, y in lista}

print(dic)
