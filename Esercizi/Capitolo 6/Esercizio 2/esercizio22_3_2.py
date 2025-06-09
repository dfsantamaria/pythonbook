# Verificare se il tipo delle variabili definite dall'esercizio 2) è il tipo int. Stampare a schermo il risultato.
# Riscrivere gli esercizi precedenti usando una funzione da includere in un modulo.

def verifica_interi():
    int1 = 1
    int2 = 2
    int3 = 3
    int4 = 4
    int5 = 5

    tutti_interi = True

    if not isinstance(int1, int):
        tutti_interi = False
    if not isinstance(int2, int):
        tutti_interi = False
    if not isinstance(int3, int):
        tutti_interi = False
    if not isinstance(int4, int):
        tutti_interi = False
    if not isinstance(int5, int):
        tutti_interi = False

    print(tutti_interi)
