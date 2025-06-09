# Stampare a schermo gli id delle variabili definite dall'esercizio 3).
# Riscrivere gli esercizi precedenti usando una funzione da includere in un modulo.

def stampa_id_stringhe():
    str1 = "ciao"
    str2 = "mondo"
    print(id(str1), id(str2))
