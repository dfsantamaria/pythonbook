# Scrivere una funzione che restituisca la media dei voti ottenuti dagli
# studenti per ogni docente e corso.

def media_voti_per_docente_e_corso(studenti, docenti):
    voti_docente = {}

    materia_docente = {}
    for d in docenti:
        materia = d["MATERIA"]
        docente = d["DOCENTE"]
        materia_docente[materia] = docente

    for s in studenti:
        materia = s["MATERIA"]
        voto = s["VOTO"]

        if materia in materia_docente:
            docente = materia_docente[materia]
            chiave = (docente, materia)

            if chiave not in voti_docente:
                voti_docente[chiave] = [voto]
            else:
                voti_docente[chiave].append(voto)

    medie = {}
    for chiave in voti_docente:
        voti = voti_docente[chiave]
        media = sum(voti) / len(voti)
        medie[chiave] = media

    return medie

studenti = [
    {"NOME": "Alice", "VOTO": 28, "MATERIA": "Matematica"},
    {"NOME": "Bob", "VOTO": 30, "MATERIA": "Fisica"},
    {"NOME": "Carla", "VOTO": 26, "MATERIA": "Matematica"},
    {"NOME": "Daniele", "VOTO": 27, "MATERIA": "Fisica"},
    {"NOME": "Elena", "VOTO": 29, "MATERIA": "Chimica"}
]

docenti = [
    {"DOCENTE": "Prof. Rossi", "MATERIA": "Matematica"},
    {"DOCENTE": "Prof. Bianchi", "MATERIA": "Fisica"},
    {"DOCENTE": "Prof.ssa Verdi", "MATERIA": "Chimica"}
]

risultato = media_voti_per_docente_e_corso(studenti, docenti)
for chiave in risultato:
    docente, materia = chiave
    print(f"{docente} - {materia}: media voti = {risultato[chiave]:.2f}")