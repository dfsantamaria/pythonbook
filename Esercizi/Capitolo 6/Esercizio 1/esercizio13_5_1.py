# Ottenere "Nome", "Cognome" ed "Eta" dalla stringa "Nome,Cognome,Età ". Fare attenzione agli spazi. Stampare a schermo il risultato.
# Riscrivere tutti gli esercizi precedenti usando una funzione
def ottieni_parti():
    s = "Nome,Cognome,Età "
    parti = s.strip().split(",")
    for parte in parti:
        print(parte)

ottieni_parti()
