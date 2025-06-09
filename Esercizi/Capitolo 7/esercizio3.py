# Scrivere una funzione che, presa una lista di L stringhe, restituisca
# una stringa costituita da tutte le stringhe della lista L ma in ordine
# inverso.
def unisci_inverso(lista):
    risultato = ""
    i = len(lista) - 1
    while i >= 0:
        risultato = risultato + lista[i]
        i = i - 1
    return risultato

parole = ["ciao", "mondo", "python"]
print(unisci_inverso(parole))








