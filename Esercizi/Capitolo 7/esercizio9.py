# Scrivere una funzione che prenda in input una sequenza di elementi
# (tupla o dizionario) con: NOME STUDENTE, VOTO DI LAUREA
# e restituisca la media del voto di laurea.

# Esercizio svolto con tupla
def media_voti(lista_studenti):
    somma = 0
    numero_studenti = 0

    for studente in lista_studenti:
        voto = studente[1]  # il voto è in posizione 1 nella tupla
        somma = somma + voto
        numero_studenti = numero_studenti + 1

    if numero_studenti == 0:
        return 0

    media = somma / numero_studenti
    return media

studenti = [("Mario", 100), ("Luca", 90), ("Anna", 110)]
print(media_voti(studenti))

#Esercizio svolto con dizionario
def media_voti(lista_studenti):
    somma = 0
    numero_studenti = 0

    for studente in lista_studenti:
        voto = studente["VOTO"]
        somma = somma + voto
        numero_studenti = numero_studenti + 1

    if numero_studenti == 0:
        return 0

    media = somma / numero_studenti
    return media

studenti = [
    {"NOME": "Mario", "VOTO": 100},
    {"NOME": "Luca", "VOTO": 90},
    {"NOME": "Anna", "VOTO": 110}
]

print(media_voti(studenti))
