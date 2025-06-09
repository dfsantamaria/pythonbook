# Scrivere una funzione che, prese due liste di caratteri, restituisca una
# stringa costituita dai caratteri delle due liste prese in ordine alternato
# (le due liste hanno la stessa dimensione).
def alterna_caratteri(lista1, lista2):
    risultato = ""
    i = 0
    while i < len(lista1):
        risultato = risultato + lista1[i] + lista2[i]
        i = i + 1
    return risultato

l1 = ['a', 'b', 'c']
l2 = ['1', '2', '3']
print(alterna_caratteri(l1, l2))
