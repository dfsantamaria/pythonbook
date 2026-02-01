# Esempio di unpacking chiave-valore di un dizionario

def saluta(Nome, Cognome, Matricola):
    print(f"{Nome}, {Cognome}, {Matricola}!")


dizionario = {"Nome": "Mario", "Cognome": "Rossi", "Matricola": 9999}
saluta(**dizionario) 