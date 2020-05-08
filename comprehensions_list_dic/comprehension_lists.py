"""
List Comprehension
"""
l1 = [1, 2, 3, 4]

l2 = [x for x in l1]
print(l2)

l3 = [x*3 for x in l1]
print(l3)

l4 = [(x, y) for x in l1 for y in range(3)]
print(l4)

l5 = ['Luiz', 'Mauro', 'Maria']
l6 = [x.replace('a', '@') for x in l5]
print(l6)

tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)

print(tupla)

l8 = [(x, y) for x, y in tupla]
print(l8)

l9 = [(y.upper(), x.upper()) for x, y in tupla]
print(l9)

l9 = dict(l9)
print(l9)

l10 = range(50)

l11 = [x for x in l10 if x % 2 == 0 and x % 3 == 0]

print(l11)

l10 = range(15)

l12 = [x if x % 5 == 0 else 0 for x in l10]
print(l12)

l13 = [x if x % 5 == 0 or x % 3 == 0 else 0 for x in l10]
print(l13)
