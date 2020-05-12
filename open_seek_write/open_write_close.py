
file = open('abc.txt', 'w+')

for numero in range(5):
    file.write(f'Linha{numero} = {numero}\n')

print(file.read())
file.close()
