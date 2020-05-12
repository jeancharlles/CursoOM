import json

with open('abc.json', 'r') as file:
    dic_json = file.read()
    dic_json = json.loads(dic_json)

for k, v in dic_json.items():
    print(f'\n{k}:')
    for k1, v1 in v.items():
        print(f'{k1}:{v1}')

