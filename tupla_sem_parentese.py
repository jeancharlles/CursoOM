tupla = 1, 2, 3, 'tupla'

print(type(tupla))

print(tupla[2:])

t1 = 1, 2, 3
t2 = 4, 5, 6

print(t1+t2)

t3 = t1 + t2

n1, n2, *_, n6 = t3

print(n6)
