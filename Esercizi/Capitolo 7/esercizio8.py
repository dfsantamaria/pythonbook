# Scrivere una funzione che, prese due liste di stringhe, restituisca una
# lista costituita dagli elementi della prima lista esclusi gli elementi che
# appartengono alla seconda lista.
def differenza_liste(lista1, lista2):
    risultato = []
    for elemento in lista1:
        if elemento not in lista2:
            risultato.append(elemento)
    return risultato

l1 = ["a", "b", "c", "d"]
l2 = ["b", "d"]
print(differenza_liste(l1, l2))
