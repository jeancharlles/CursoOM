lista = [['P1', 11], ['P2', 15], ['P3', 18], ['P4', 19], ['P5', 12]]

lista.sort(key=lambda item: item[1])
# lista.sort(key=lambda item: item[1], reverse=True)  # para imprimir em ordem inversa

print(lista)
