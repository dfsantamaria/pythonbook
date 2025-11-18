# Esempio di unpacking chiave-valore di un dizionario

dizionario = {"Nome": "Mario", "Cognome": "Rossi", "Matricola": 9999}
dizionario2 = {**dizionario, "Corso": "Informatica"}
print(dizionario2) 