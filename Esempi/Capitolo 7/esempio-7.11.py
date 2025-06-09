# Modifica di una lista attraverso uan funzione

def modifica_lista(lista: list, pos: int, val):
    lista[pos] = val


lista = [3, 5, "test"]
modifica_lista(lista, 2, 90)
print(lista)