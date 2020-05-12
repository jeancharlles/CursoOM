
file = open('abc.txt', 'r')

file.seek(0, 0)

print(file.read())

file.close()
