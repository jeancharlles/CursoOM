
file = open('abc.txt', 'r')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

print(f'-'*20)

file.seek(0, 0)
print(file.read())

file.close()
