lista = [3, 5, 10, -1, 5, -10, 25]
for elem in lista:
    print(elem)

for pos, elem in enumerate(lista):
    print(pos, elem)

for pos in range(0, len(lista)):
    print(pos, lista[pos])