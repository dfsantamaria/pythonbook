# Data una stringa inserita dall'utente, stampare tutti i caratteri in posizione pari della stringa.
s = input('Inserisci una stringa: ')
for i in range(0, len(s), 2):
    print(s[i])
