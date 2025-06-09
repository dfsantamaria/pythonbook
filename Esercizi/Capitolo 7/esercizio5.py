# Scrivere una funzione che, prese due liste di caratteri, restituisca una
# stringa costituita dai caratteri delle due liste prese in ordine alternato.
# Le due liste possono avere dimensioni diverse. In questo caso inserire
# i caratteri rimanenti della lista più grande a fine stringa.
def alterna_caratteri_estesa(lista1, lista2):
    risultato = ""
    i = 0
    while i < len(lista1) and i < len(lista2):
        risultato = risultato + lista1[i] + lista2[i]
        i = i + 1

    while i < len(lista1):
        risultato = risultato + lista1[i]
        i = i + 1

    while i < len(lista2):
        risultato = risultato + lista2[i]
        i = i + 1

    return risultato

l1 = ['a', 'b', 'c', 'd']
l2 = ['1', '2']
print(alterna_caratteri_estesa(l1, l2))
