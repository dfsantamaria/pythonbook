# Scrivere una funzione che restituisca per ogni corso di laurea presente
# la media del voto di laurea.

#Esercizio svolto con dizionari
def media_per_corso(studenti):
    corsi = {}
    conteggi = {}

    for studente in studenti:
        corso = studente["CORSO"]
        voto = studente["VOTO"]

        if corso not in corsi:
            corsi[corso] = voto
            conteggi[corso] = 1
        else:
            corsi[corso] = corsi[corso] + voto
            conteggi[corso] = conteggi[corso] + 1

    medie = {}
    for corso in corsi:
        medie[corso] = corsi[corso] / conteggi[corso]

    return medie

studenti = [
    {"NOME": "Mario", "VOTO": 100, "CORSO": "Informatica"},
    {"NOME": "Luca", "VOTO": 90, "CORSO": "Fisica"},
    {"NOME": "Anna", "VOTO": 110, "CORSO": "Informatica"},
    {"NOME": "Giulia", "VOTO": 100, "CORSO": "Fisica"}
]

print(media_per_corso(studenti))

#Esercizio svolto con tuple
def media_per_corso(studenti):
    corsi = {}
    conteggi = {}

    for studente in studenti:
        nome = studente[0]
        voto = studente[1]
        corso = studente[2]

        if corso not in corsi:
            corsi[corso] = voto
            conteggi[corso] = 1
        else:
            corsi[corso] = corsi[corso] + voto
            conteggi[corso] = conteggi[corso] + 1

    medie = {}
    for corso in corsi:
        media = corsi[corso] / conteggi[corso]
        medie[corso] = media

    return medie

studenti = [
    ("Mario", 100, "Informatica"),
    ("Luca", 90, "Fisica"),
    ("Anna", 110, "Informatica"),
    ("Giulia", 100, "Fisica")
]

print(media_per_corso(studenti))