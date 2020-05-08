"""
Os sets ou conjuntos somente aceitam valores imutáveis e únicos.

Ou seja não aceitam listas, dicionários ou mais de um elemento.

O set elimina valores repetidos.

Aceitam valores como inteiros, strings, floats e tuplas.

"""

# Exemplo 7 - Update - Atualiza um set com novos valores, com a possibilidade de inserir mais de um elemento
print()
s7 = {1, 2, 3}
s7.update([4, 5], {'chave': 7})  # Aceita elementos iteráveis como listas e dicionários
s7.add(6)  # Aceita somente elementos imutáveis e únicos
print(f's7={s7}')

# Exemplo 8 - Intersection - interseção entre dois conjuntos/sets
print()
s8 = {1, 2, 3, 4}
print(f's8={s8}')
s8.intersection(s7)
print(f's8.intersection(s7) = {s8}')

# Exemplo 9 - Discard - retirando valor do conjunto
print()
s9 = {1, 2, 3, 4}
print(f's9={s9}')
s9.discard(3)
print(f's9.discard(3)= {s9}')
