# Data una stringa inserita dall'utente, stampare tutti i caratteri in posizione dispari della stringa.
# Riscrivere tutti gli esercizi precedenti usando una funzione da includere in un modulo
def stampa_caratteri_dispari():
    s = input('Inserisci una stringa: ')
    for i in range(1, len(s), 2):
        print(s[i])