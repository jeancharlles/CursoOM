from modulo_os.conversor_byte import formata_tamanho
import os

# caminho_procura = '/home/jean/PycharmProjects/CursoOM/modulo_os/'
# caminho_procura = './'
# termo_procura = 'Cap'

caminho_procura = input('Digite o caminho do arquivo: ')
termo_procura = input('Digite o nome do arquivo: ')
conta = 0


for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                print(f'\nArquivo encontrado: {arquivo}')
                caminho_completo = os.path.join(raiz, arquivo)
                print(f'Caminho completo do arquivo: {caminho_completo}')
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                print(f'Nome do arquivo sem extensão: {nome_arquivo}')
                print(f'Extensão do arquivo: {ext_arquivo}')
                print(f'Tamanho do arquivo em bytes: {tamanho}')
                print(f'Tamanho formatado: {formata_tamanho(tamanho)}')
                print(f'-'*50)

            except PermissionError as erro:
                print('Erro de Permissão')
            except FileNotFoundError as erro:
                print('Arquivo não encontrado')
            except Exception as erro:
                print(f'Erro desconhecido: {erro}')


print()
print(f'{conta} arquivo(s) encontrado(s).')
