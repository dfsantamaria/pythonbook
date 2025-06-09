# Usare f-string per formattare una stringa contenente nome, cognome, età, numero di matricola e numero di cellulare di uno studente. Stampare a schermo il risultato.
# Riscrivere tutti gli esercizi precedenti usando una funzione da includere in un modulo
def formatta_studente():
    nome = "Mario"
    cognome = "Rossi"
    eta = 22
    matricola = "12345"
    cellulare = "3331234567"
    print(f"{nome} {cognome}, {eta} anni, matricola {matricola}, cell: {cellulare}")
