#List Comprehension con filtro
def crea_lista(lista: list) -> list:
    lista2 = [elem for elem in lista if elem > 0]
    return lista2


lista = [3, 5, 10, -1, 5, -10, 25]
lista2 = crea_lista(lista)
print(lista2)