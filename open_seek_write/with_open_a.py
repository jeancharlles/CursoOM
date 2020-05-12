
with open('abc.txt', 'a+') as file:
    file.seek(0, 0)
    file.write('\n')
    file.write('Com a+ o conteúdo é adicionado, sem apagar o conteúdo anterior.')

    file.seek(0, 0)
    print(file.read(), end='')
    file.close()
