string = 'O Brasil é Penta.'
lista = string.split(' ')  # em cada espaço será separado

for indice, valor in enumerate(lista):
    print(indice, valor)

print()

for indice, valor in enumerate(lista):
    print(indice, lista[indice])
