string = 'O Brasil é o pais do futebol, e o Brasil é Penta.'
lista1 = string.split(' ')  # em cada espaço será separado
lista2 = string.split(',')  # em cada vírgula será separado
print(lista2)

for palavra in lista1:
    print(f'A palavra {palavra} apareceu {lista1.count(palavra)}x na frase.')


