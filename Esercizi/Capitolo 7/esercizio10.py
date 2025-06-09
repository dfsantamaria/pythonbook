# Scrivere una funzione che restituisca l’elenco degli studenti che hanno
# avuto un voto di laurea non inferiore a 100.

#Esercizio svolto con tupla
def studenti_eccellenti(lista_studenti):
    risultato = []
    for studente in lista_studenti:
        nome = studente[0]
        voto = studente[1]
        if voto >= 100:
            risultato.append(nome)
    return risultato

studenti = [
    ("Mario", 100),
    ("Luca", 90),
    ("Anna", 110)
]

print(studenti_eccellenti(studenti))

#Esercizio svolto con dizionario
def studenti_eccellenti(lista_studenti):
    risultato = []
    for studente in lista_studenti:
        if studente["VOTO"] >= 100:
            risultato.append(studente["NOME"])
    return risultato

# Esempio d'uso
studenti = [
    {"NOME": "Mario", "VOTO": 100},
    {"NOME": "Luca", "VOTO": 90},
    {"NOME": "Anna", "VOTO": 110}
]

print(studenti_eccellenti(studenti))


