# Verificare se il tipo delle variabili definite dall'esercizio 4) è il tipo bool. Stampare a schermo il risultato.
# Riscrivere gli esercizi precedenti usando una funzione da includere in un modulo.

def verifica_booleani():
    bool1 = True
    bool2 = False

    sono_booleani = True

    if not isinstance(bool1, bool):
        sono_booleani = False
    if not isinstance(bool2, bool):
        sono_booleani = False

    print(sono_booleani)
