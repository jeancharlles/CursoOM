try:
    file = open('abc.txt', 'w+')
    file.write('DEF')
except Exception as erro:
    print('Arquivo não aberto')
finally:
    file = open('abc.txt', 'r')
    file.seek(0, 0)
    print(file.read())
    file.close()
