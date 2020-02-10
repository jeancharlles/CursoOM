variavel = ['Jean', 'Isabella', 'Claudia']

for valor in variavel:
    if valor.lower().startswith('j'):
        print(f'Existe uma palavra que comeca com J')
        print(valor)
        break
else:
    print(f'Não existe uma palavra que comeca com J')
