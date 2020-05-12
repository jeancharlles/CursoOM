
file = open('abc.txt', 'r')

file.seek(0, 0)
print(f'\nImpressão em Lista')
print(file.readlines())
print(f'-'*60)

file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')

file.close()
