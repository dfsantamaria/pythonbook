#List Comprehension con espressione condizionale
def crea_lista(lista: list) -> list:
    lista2 = [elem if elem > 0 else None for elem in lista]
    return lista2


lista = [3, 5, 10, -1, 5, -10, 25]
lista2 = crea_lista(lista)
print(lista2)