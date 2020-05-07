lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
]

dic = {chave.upper(): valor.upper() for chave, valor in lista}

print(dic)

dic = {chave: valor*2 for chave, valor in enumerate(range(10))}
print(dic)
