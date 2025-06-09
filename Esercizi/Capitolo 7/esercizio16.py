# Scrivere una funzione che prende due liste: nomi completi e date di nascita.
# Restituisce una lista di dizionari con NOME COMPLETO (tupla) e DATA NASCITA.

def crea_lista_dizionari(nomi, date_nascita):
    risultato = []
    for i in range(len(nomi)):
        nome_completo = nomi[i].split()
        nome = nome_completo[0]
        cognome = nome_completo[1]
        data = date_nascita[i]
        studente = {
            "NOME COMPLETO": (nome, cognome),
            "DATA NASCITA": data
        }
        risultato.append(studente)
    return risultato

nomi = ["Mario Rossi", "Luca Bianchi", "Anna Verdi"]
date = ["01/01/2000", "15/03/1999", "20/05/2001"]

print(crea_lista_dizionari(nomi, date))