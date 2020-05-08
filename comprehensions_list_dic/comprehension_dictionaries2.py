lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
]

dic = {chave.upper(): valor.upper() for chave, valor in lista}

print(dic)

dic = {chave: valor*2 for chave, valor in enumerate(range(10))}
print(dic)

# Se não especificar a chave, passando somente o valor, o resultado será a criação de Sets
# Set com enumerate
dic = {valor for valor in enumerate(range(10))}
print(dic)
print(type(dic))

# Set somente com range
dic = {valor for valor in (range(10))}
print(dic)
print(type(dic))

# Gerando dicionários com uma variável apenas
dic = {f'chave_{x}': x+1 for x in (range(5))}
print(dic)
