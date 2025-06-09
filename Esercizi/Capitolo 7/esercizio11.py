# Scrivere una funzione che restituisca l’elenco degli studenti che hanno
# avuto un voto di laurea non inferiore a 100 e il relativo voto conseguito.

#Esercizio svolto con tuple
def studenti_eccellenti_con_voto(lista_studenti):
    risultato = []
    for studente in lista_studenti:
        nome = studente[0]
        voto = studente[1]
        if voto >= 100:
            risultato.append((nome, voto))
    return risultato

studenti = [
    ("Mario", 100),
    ("Luca", 90),
    ("Anna", 110)
]

print(studenti_eccellenti_con_voto(studenti))

#Esercizio svolto con dizionari
def studenti_eccellenti_con_voto(lista_studenti):
    risultato = []
    for studente in lista_studenti:
        if studente["VOTO"] >= 100:
            risultato.append({"NOME": studente["NOME"], "VOTO": studente["VOTO"]})
    return risultato

studenti = [
    {"NOME": "Mario", "VOTO": 100},
    {"NOME": "Luca", "VOTO": 90},
    {"NOME": "Anna", "VOTO": 110}
]

print(studenti_eccellenti_con_voto(studenti))