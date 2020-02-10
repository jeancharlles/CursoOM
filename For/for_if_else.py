variavel = ['Jean', 'Isabella', 'Claudia']
comeca_com_j = False

for valor in variavel:
    if valor.lower().startswith('j'):
        comeca_com_j = True

if comeca_com_j:
    print(f'Existe uma palavra que comeca com J')
else:
    print(f'Não existe uma palavra que comeca com J')
