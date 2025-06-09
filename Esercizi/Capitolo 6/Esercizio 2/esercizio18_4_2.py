# Data una stringa inserita dall'utente, stampare tutti i caratteri in posizione pari della stringa.
# Riscrivere tutti gli esercizi precedenti usando una funzione da includere in un modulo
def stampa_caratteri_pari():
    s = input('Inserisci una stringa: ')
    for i in range(0, len(s), 2):
        print(s[i])

