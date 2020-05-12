
try:
    file = open('def.txt', 'w+')
    file.write('DEF')
except Exception as erro:
    print('Arquivo não aberto')
finally:
    file = open('def.txt', 'r')
    file.seek(0, 0)
    print(file.read())
    file.close()
