# Stampare a schermo i numeri da 1 a 30
# interropendo il ciclo quando si incontra il primo numero pari.
# Riscrivere tutti gli esercizi precedenti usando una funzione da includere in un modulo
def stampa_fino_primo_pari():
    for i in range(1, 31):
        print(i)
        if i % 2 == 0:
            break
