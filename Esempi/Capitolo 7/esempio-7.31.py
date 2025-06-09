# Esempio di packing chiave-valore di un
# dizionario

def stampa(**coppie):
    for chiave, valore in coppie.items():
        print(f"{chiave}: {valore}")


stampa(nome="Mario", cognome="Rossi", matricola=9999)