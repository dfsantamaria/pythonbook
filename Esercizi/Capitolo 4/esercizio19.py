# Data una stringa inserita dall'utente, stampare tutti i caratteri in posizione dispari della stringa.
s = input('Inserisci una stringa: ')
for i in range(1, len(s), 2):
    print(s[i])
