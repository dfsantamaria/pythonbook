#Creazione di una lista a partire da una lista data
def crea_lista(lista: list) -> list:
    lista2 = []
    for elem in lista:
        if elem > 0:
            lista2.append(elem)
        else:
            lista2.append(None)
    return lista2


lista = [3, 5, 10, -1, 5, -10, 25]
lista2 = crea_lista(lista)
print(lista2)