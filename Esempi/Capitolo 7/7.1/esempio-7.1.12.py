# Modifica di una lista attraverso una funzione

def modifica_lista(lista: list, pos: int, val):
    lista[pos] = val
#fine definizione funzione

lista = [3, 5, "test"]
modifica_lista(lista, 2, 90)
print(lista)