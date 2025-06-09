# Scrivere una funzione che restituisca il/i docente/i i cui studenti hanno
# ottenuto la media più alta.

def docente_con_media_piu_alta(studenti, docenti):
    materia_docente = {}
    voti_docente = {}
    conteggio_docente = {}
    for d in docenti:
        materia_docente[d["MATERIA"]] = d["DOCENTE"]

    for s in studenti:
        materia = s["MATERIA"]
        voto = s["VOTO"]
        docente = materia_docente.get(materia)

        if docente:
            if docente not in voti_docente:
                voti_docente[docente] = voto
                conteggio_docente[docente] = 1
            else:
                voti_docente[docente] += voto
                conteggio_docente[docente] += 1

    medie_docenti = {}
    for docente in voti_docente:
        media = voti_docente[docente] / conteggio_docente[docente]
        medie_docenti[docente] = media

    max_media = max(medie_docenti.values())

    docenti_top = []
    for docente in medie_docenti:
        if medie_docenti[docente] == max_media:
            docenti_top.append(docente)

    return docenti_top

studenti = [
    {"NOME": "Alice", "VOTO": 28, "MATERIA": "Matematica"},
    {"NOME": "Bob", "VOTO": 30, "MATERIA": "Fisica"},
    {"NOME": "Carla", "VOTO": 26, "MATERIA": "Matematica"},
    {"NOME": "Daniele", "VOTO": 30, "MATERIA": "Fisica"},
    {"NOME": "Elena", "VOTO": 29, "MATERIA": "Chimica"}
]

docenti = [
    {"DOCENTE": "Prof. Rossi", "MATERIA": "Matematica"},
    {"DOCENTE": "Prof. Bianchi", "MATERIA": "Fisica"},
    {"DOCENTE": "Prof.ssa Verdi", "MATERIA": "Chimica"}
]

print(docente_con_media_piu_alta(studenti, docenti))