# Esempio sull'uso di setdefault

dizionario = {"Nome": "Mario", "Cognome": "Rossi", "Matricola": 9999}
print(dizionario.setdefault("Nome", "Mario"))  # restituisce "Mario", già presente
print(dizionario.setdefault("Matricola", 1000))  # crea una nuova voce, "Matricola" non è presente