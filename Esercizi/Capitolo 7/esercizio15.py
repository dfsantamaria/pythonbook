# Scrivere una funzione che prende in input una lista di stringhe,
# ciascuna contenente le informazioni: NOME, COGNOME, DATA NASCITA.

def crea_dizionari_info(lista_stringhe):
    risultato = []
    for stringa in lista_stringhe:
        parti = stringa.split(",")
        nome = parti[0].strip()
        cognome = parti[1].strip()
        data_nascita = parti[2].strip()
        studente = {
            "NOME": nome,
            "COGNOME": cognome,
            "DATA NASCITA": data_nascita
        }
        risultato.append(studente)
    return risultato

dati = [
    "Mario, Rossi, 01/01/2000",
    "Luca, Bianchi, 15/03/1999",
    "Anna, Verdi, 20/05/2001"
]

print(crea_dizionari_info(dati))
