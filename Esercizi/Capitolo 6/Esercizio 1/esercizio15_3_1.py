# Stampare a schermo gli id delle variabili definite dall'esercizio 3).
# Riscrivere tutti gli esercizi precedenti usando una funzione.

def stampa_id_stringhe():
    str1 = "ciao"
    str2 = "mondo"
    print(id(str1), id(str2))

stampa_id_stringhe()
