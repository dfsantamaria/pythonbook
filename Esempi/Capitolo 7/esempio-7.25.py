# Esempio di iterazione sulle voci di un dizionario

dizionario = {"Nome": "Mario", "Cognome": "Rossi", "Matricola": 9999}

for chiave in dizionario:
    print(chiave)  # accediamo ad ogni singola chiave

for valore in dizionario.values():
    print(valore)  # accediamo ad ogni singolo valore

for tupla in dizionario.items():
    print(tupla)  # accediamo ad ogni singola coppia chiave-valore in formato tupla
