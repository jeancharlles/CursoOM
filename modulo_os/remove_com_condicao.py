
import os

caminho_antigo = '/home/jean/PycharmProjects/CursoOM/modulo_os/antiga_pasta'
caminho_novo = '/home/jean/PycharmProjects/CursoOM/modulo_os/nova_pasta'

try:
    os.mkdir(caminho_novo)
    print('Pasta criada com sucesso!')
except FileExistsError as erro:
    print(f'Esta pasta {caminho_novo} já existe!')
except Exception as erro:
    print(erro)

for root, dirs, files in os.walk(caminho_antigo):
    for file in files:
        print(f'\n{file} está no caminho antigo')
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        try:
            if '.py' in file:
                os.remove(new_file_path)
                print(f'Arquivo {file} foi removido com sucesso!')
        except FileNotFoundError as erro:
            print(f'{erro} - Arquivo {file} não encontrado.')

