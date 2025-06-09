# Data la stringa inserita dall'utente, stampare i caratteri della stringa, a due a due, saltando due caratteri.
# Ad esempio, presa la stringa 'messaggio', stampare in ordine 'me', 'ag', 'o'.
# Riscrivere tutti gli esercizi precedenti usando una funzione da includere in un modulo
def stampa_due_a_due_saltando():
    testo = input("Inserisci una stringa: ")
    i = 0
    while i < len(testo):
        coppia = testo[i:i+2]
        print(coppia)
        i += 4