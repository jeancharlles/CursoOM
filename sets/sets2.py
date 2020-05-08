"""
Os sets ou conjuntos somente aceitam valores imutáveis e únicos.

Ou seja não aceitam listas, dicionários ou mais de um elemento.

O set elimina valores repetidos.

Aceitam valores como inteiros, strings, floats e tuplas.

"""

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

