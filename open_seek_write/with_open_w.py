
with open('abc.txt', 'w+') as file:
    file.seek(0, 0)
    file.write('Com o w+ o conteúdo anterior é apagado e sobrescrito com o novo conteúdo')

    file.seek(0, 0)
    print(file.read(), end='')
    file.close()
