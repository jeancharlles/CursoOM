string = 'O Brasil é o o o pais do futebol, e o Brasil é Penta.'
lista1 = string.split(' ')  # em cada espaço será separado
lista2 = string.split(',')  # em cada vírgula será separado
print(lista2)
palavra = ''
contagem = 0

for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é: \"{palavra}\" e aparaeceu {contagem} vezes.')


