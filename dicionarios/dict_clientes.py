clientes = {
    'cliente1': {'nome': 'ana', 'sobrenome': 'maria'},
    'cliente2': {'nome': 'jose', 'sobrenome': 'maria'}
}

for cliente_k, cliente_v in clientes.items():
    print(f'\nExibindo: {cliente_k}')
    for dados_k, dados_v in cliente_v.items():
        print(f'\t{dados_k} = {dados_v}')
