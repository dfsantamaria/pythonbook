# Esempio di unpacking chiave-valore di un dizionario

def saluta(Cognome, Nome):
    print(f"{Nome}, {Cognome}, {Matricola}!")


dizionario = {"Nome": "Mario", "Cognome": "Rossi", "Matricola": 9999}
saluta(**dizionario) 