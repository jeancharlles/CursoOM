
file = open('abc.txt', 'r')

file.seek(0, 0)

for linha in file:
    print(linha, end='')
