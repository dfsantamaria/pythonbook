# Usare gli operatori aritmetici per effettuare delle operazioni sulle variabili definite dall'esercizio 2),
# salvando il nuovo valore su una nuova variabile. Stampare il contenuto e l'id della nuova variabile.
# Riscrivere tutti gli esercizi precedenti usando una funzione.

def operazioni_float():
    int1 = 1
    int2 = 2
    int3 = 3
    int4 = 4
    int5 = 5
    nuovo_val = int1 * int2 + int3 - int4
    print(nuovo_val, id(nuovo_val))

operazioni_interi()
