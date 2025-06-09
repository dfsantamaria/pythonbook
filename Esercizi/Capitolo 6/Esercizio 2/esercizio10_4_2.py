# Stampare a schermo i numeri da 1 a 20 ad eccezione dei multipli di 3.
# Riscrivere tutti gli esercizi precedenti usando una funzione da includere in un modulo
def stampa_non_multipli_di_3():
    for i in range(1, 21):
        if i % 3 != 0:
            print(i)

