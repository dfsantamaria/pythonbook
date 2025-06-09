# Stampare a schermo gli id delle variabili definite dall'esercizio 2).
# Riscrivere tutti gli esercizi precedenti usando una funzione.

def stampa_id_interi():
    int1 = 1
    int2 = 2
    int3 = 3
    int4 = 4
    int5 = 5
    print(id(int1), id(int2), id(int3), id(int4), id(int5))

stampa_id_interi()
