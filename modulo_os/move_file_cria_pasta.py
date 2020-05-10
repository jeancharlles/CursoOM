
import os
import shutil

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
        print(f'\n{file}')
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        shutil.move(old_file_path, new_file_path)
        print(f'Arquivo {file} foi movido com sucesso!')
