import json

dic = {
    'Pessoa1': {
        'nome': 'maria',
        'idade': 20,
    },
    'Pessoa2': {
        'nome': 'ana',
        'idade': 22,
    }
}
print(dic)

dic_json = json.dumps(dic, indent=True)
print(dic_json)

with open('abc.json', 'w+') as file:
    file.write(dic_json)
    print('Arquivo criado com sucesso!')
