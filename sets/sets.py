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
