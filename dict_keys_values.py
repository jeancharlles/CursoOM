dic1 = {
    1: 'valor 1',
    'str': 'valor 2',
    (1, 2, 3): 'valor 3'
}

# Usando keys
if 1 in dic1.keys():
    print('A chave 1 existe no dicionário')
else:
    print('A chave 1 não existe no dicionário')


# Usando values
if 'valor 3' in dic1.values():
    print('O valor 3 existe no dicionário')
else:
    print('O valor 3 não existe no dicionário')

print(len(dic1))
