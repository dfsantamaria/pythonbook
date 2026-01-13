# Data la stringa inserita dall'utente, stampare i caratteri della stringa, a due a due, saltando due caratteri. Ad esempio, presa la stringa "messaggio",
# stampare in ordine me, ag, o.
testo = input("Inserisci una stringa: ")
i = 0
while i < len(testo):
    j = 0
    coppia = ''
    while j <= 1 and i+j < len(testo):
        coppia+=testo[i+j]
        j += 1
    print(str)
    i += 4
