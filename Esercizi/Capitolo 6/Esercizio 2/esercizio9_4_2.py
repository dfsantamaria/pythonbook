# Stampare i numeri da 1 a 100 divisibili per 10.
# Riscrivere tutti gli esercizi precedenti usando una funzione da includere in un modulo
def stampa_divisibili_per_10():
    for i in range(1, 101):
        if i % 10 == 0:
            print(i)

