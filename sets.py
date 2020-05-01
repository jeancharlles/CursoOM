"""
Os sets ou conjuntos somente aceitam valores imutáveis e únicos.

Ou seja não aceitam listas, dicionários ou mais de um elemento.

O set elimina valores repetidos.

Aceitam valores como inteiros, strings, floats e tuplas.

"""
# Exemplo 1 - Criando Sets
s1 = set()
s2 = {1, 2, 3}
print(type(s1))
print(f's1={s1}')
print(f's2={s2}')

# Exemplo 2 - Adcionando valores no set com add
print()
s3 = set()
s3.add((1, 2, 3, 4))
print(f's3={s3}')
s3.add(5)
print(f's3={s3}')

# Exemplo 3 - Adcionando valores com pipeline
print()
s4 = {1, 2, 3, 4, 5}
print(f's4={s4}')
print()
s4 = {1, 2, 3, 4, 5} | s3
print(f's4|s3={s4}')

# Exemplo 4 - Unindo sets usando union
print()
s5 = s4
s5.union(s3)
print(f's5.union(s3)= {s5}')


# Exemplo 5 - Diferença entre sets, prevalece o da esquerda
print()
print(f's5={s5}')
s6 = {1, 2, 3, 4, 5, 6, 7.0}
print(f's6={s6}')
print()
print(f's6-s5 = {s6-s5}')

# Exemplo 6 - Diferença entre sets, usando difference, prevalece o da esquerda
print(f's5.difference(s6) = {s5.difference(s6)}')


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
