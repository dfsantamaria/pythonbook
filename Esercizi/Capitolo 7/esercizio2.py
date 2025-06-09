# Scrivere una funzione che, presa una lista di stringhe, restituisca una
# stringa costituita dal primo e dall’ultimo carattere di ogni elemento
# della lista.
def primi_e_ultimi(lista):
    risultato = ""
    for parola in lista:
        if len(parola) >= 2:
            risultato = risultato + parola[0] + parola[-1]
    return risultato

parole = ["ciao", "mondo", "python"]
print(primi_e_ultimi(parole))
