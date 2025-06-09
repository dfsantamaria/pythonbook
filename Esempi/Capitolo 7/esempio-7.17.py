# Esempio di packing di una tupla come argomento di una funzione

def stampa_tutti(messaggio, *tupla):
    print(messaggio)


for elem in tupla:
    print(elem)
stampa_tutti("Elenco:", 1, 2, 3, 4, 5)