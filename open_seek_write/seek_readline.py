
file = open('abc.txt', 'r')

file.seek(0, 0)

print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

file.close()
