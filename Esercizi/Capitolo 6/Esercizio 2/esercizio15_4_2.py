# Stampare a schermo i primi 10 numeri dispari.
# Riscrivere tutti gli esercizi precedenti usando una funzione da includere in un modulo
def primi_10_dispari():
    n = 1
    contatore = 0
    while contatore < 10:
        if n % 2 != 0:
            print(n)
            contatore += 1
        n += 1