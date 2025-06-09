# Data una stringa inserita dall'utente, stampare tutti i caratteri a partire dall'ultimo.
# Riscrivere tutti gli esercizi precedenti usando una funzione da includere in un modulo
def stampa_caratteri_inversi():
    s = input('Inserisci una stringa: ')
    for c in reversed(s):
        print(c)