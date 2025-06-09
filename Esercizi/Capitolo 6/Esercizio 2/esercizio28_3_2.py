# Concatenare le due stringhe definite dall'esercizio 3),
# ripetere la concatenazione 10 volte (con l'operatore *) e stampare a schermo. Stampare a schermo la lunghezza della stringa ottenuta.
# Stampare a schermo il carattere in posizione 5, 4 e 3 della stringa ottenuta.
# Riscrivere gli esercizi precedenti usando una funzione da includere in un modulo.

def concatena_ripeti():
    str1 = "ciao"
    str2 = "mondo"
    long_str = (str1 + str2) * 10
    print(long_str)
    print(len(long_str))
    print(long_str[5], long_str[4], long_str[3])
