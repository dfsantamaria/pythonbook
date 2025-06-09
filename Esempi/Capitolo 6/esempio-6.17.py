# Lettura di file riga per riga

with open("dati.txt", "r") as f:
    for riga in f:
        print(riga.strip())