d1 = dict()
d1['existe'] = '123'

if 'existe' not in d1:
    print('Não existe dentro do dicionário')
else:
    print('Existe no dicionário')

if d1.get('existe') is None:
    print('Não existe dentro do dicionário')
else:
    print('Existe no dicionário')

d1.update({'nova_chave': 'novo_valor'})

print(d1)

del d1['existe']
print(d1)
